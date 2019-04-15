<template>
    <el-container>
        <el-main>
            <el-input
                    placeholder="请输入内容"
                    v-model="up"
                    clearable>
            </el-input>
            <el-button v-on:click="fetchCouplet" type="primary">对下联</el-button>
            <el-card shadow="hover">
                <span>{{down}}</span>
            </el-card>
        </el-main>
    </el-container>
</template>

<script>
import $backend from '../backend'

export default {
  name: 'Couplet',
  data () {
    return {
      up: '',
      down: '',
      error: ''
    }
  },
  methods: {
    fetchCouplet () {
      // this.down = this.up
      $backend.fetchCouplet(this.up).then(responseData => {
        this.down = responseData.output
      }).catch(error => {
        this.error = error.message
      })
    }
  }
}
</script>

<style scoped>
    .el-header {
        background-color: #B3C0D1;
        color: #333;
        line-height: 60px;
    }

    .el-aside {
        color: #333;
    }
</style>
