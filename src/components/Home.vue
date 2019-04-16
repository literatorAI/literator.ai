<template>

        <el-row>
            <el-col :span="24">
                <mavon-editor v-model="value" :subfield="prop.subfield"
                          :defaultOpen="prop.defaultOpen"
                          :toolbarsFlag="prop.toolbarsFlag"
                          :editable="prop.editable"
                          :boxShadow="prop.boxShadow"
                          :scrollStyle="prop.scrollStyle"/>
            </el-col>
        </el-row>

</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  },
  data () {
    return {
      value: `# literator.AI
## 欢迎来到literator.AI,网站建设中，目前提供AI对联功能
`
    }
  },
  computed: {
    prop () {
      let data = {
        subfield: false, // 单双栏模式
        defaultOpen: 'preview', // edit： 默认展示编辑区域 ， preview： 默认展示预览区域
        editable: false,
        toolbarsFlag: false,
        // scrollStyle: true,
        boxShadow: false
      }
      return data
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
    h3 {
        margin: 40px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
