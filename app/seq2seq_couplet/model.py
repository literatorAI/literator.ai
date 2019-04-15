
import tensorflow as tf
import app.seq2seq_couplet.seq2seq as seq2seq
import app.seq2seq_couplet.reader as reader
from os import path
import random


class Model():

    def __init__(self, train_input_file, train_target_file,
            test_input_file, test_target_file, vocab_file,
            num_units, layers, dropout,
            batch_size, learning_rate, output_dir,
            save_step = 100, eval_step = 1000,
            param_histogram=False, restore_model=False,
            init_train=True, init_infer=False):
        self.num_units = num_units
        self.layers = layers
        self.dropout = dropout
        self.batch_size = batch_size
        self.learning_rate = learning_rate
        self.save_step = save_step
        self.eval_step = eval_step
        self.param_histogram = param_histogram
        self.restore_model = restore_model
        self.init_train = init_train
        self.init_infer = init_infer

        if init_train:
            self.train_reader = reader.SeqReader(train_input_file,
                    train_target_file, vocab_file, batch_size)
            self.train_reader.start()
            self.train_data = self.train_reader.read()
            self.eval_reader = reader.SeqReader(test_input_file, test_target_file,
                    vocab_file, batch_size)
            self.eval_reader.start()
            self.eval_data = self.eval_reader.read()

        self.model_file = path.join(output_dir, 'model.ckpl')
        self.log_writter = tf.summary.FileWriter(output_dir)

        if init_infer:
            self.infer_vocabs = reader.read_vocab(vocab_file)
            self.infer_vocab_indices = dict((c, i) for i, c in
                    enumerate(self.infer_vocabs))
            self._init_infer()
            self.reload_infer_model()


    def gpu_session_config(self):
        config = tf.ConfigProto()
        config.gpu_options.allow_growth = True
        return config

    def _init_infer(self):
        self.infer_graph = tf.Graph()
        with self.infer_graph.as_default():
            self.infer_in_seq = tf.placeholder(tf.int32, shape=[1, None])
            self.infer_in_seq_len = tf.placeholder(tf.int32, shape=[1])
            self.infer_output = seq2seq.seq2seq(self.infer_in_seq,
                    self.infer_in_seq_len, None, None,
                    len(self.infer_vocabs),
                    self.num_units, self.layers, self.dropout)
            self.infer_saver = tf.train.Saver()
        self.infer_session = tf.Session(graph=self.infer_graph,
                config=self.gpu_session_config())


    def reload_infer_model(self):
        with self.infer_graph.as_default():
            self.infer_saver.restore(self.infer_session, self.model_file)


    def infer(self, text):
        if not self.init_infer:
            raise Exception('Infer graph is not inited!')
        with self.infer_graph.as_default():
            in_seq = reader.encode_text(text.split(' ') + ['</s>',],
                    self.infer_vocab_indices)
            in_seq_len = len(in_seq)
            outputs = self.infer_session.run(self.infer_output,
                    feed_dict={
                        self.infer_in_seq: [in_seq],
                        self.infer_in_seq_len: [in_seq_len]})
            output = outputs[0]
            output_text = reader.decode_text(output, self.infer_vocabs)
            return output_text
