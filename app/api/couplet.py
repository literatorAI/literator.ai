from datetime import datetime
from flask import Flask, jsonify, request
from flask_restplus import Resource
from . import api_rest
from app.seq2seq_couplet.model import Model

vocab_file = 'data/couplet/vocabs'
model_dir = 'data/models/tf-lib/output_couplet'

m = Model(
    None, None, None, None, vocab_file,
    num_units=1024, layers=4, dropout=0.2,
    batch_size=32, learning_rate=0.0001,
    output_dir=model_dir,
    restore_model=True, init_train=False, init_infer=True)
print("init every time")

@api_rest.route('/couplet/<string:up>')
class Couplet(Resource):

    def get(self, up):
        if len(up) == 0 or len(up) > 50:
            output = u'您的输入太长了'
        else:
            output = m.infer(' '.join(up))
            output = ''.join(output.split(' '))
        print('上联：%s；下联：%s' % (up, output))
        return jsonify({'output': output})
        #timestamp = datetime.utcnow().isoformat()
        #return {'timestamp': timestamp}
