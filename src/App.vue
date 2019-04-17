<template>
    <div id="app">

        <el-container>
            <el-header>
                <div id="nav">
                    <router-link to="/">Home</router-link> |
                    <router-link to="/couplet">Couplet</router-link>
                </div>
                <!-- FORK Me -->
                <a href="https://github.com/literatorAI/literator.ai"><img
                        style="position: absolute; top: 0; right: 0; border: 0;z-index: 100000"
                        src="@/assets/forkme_right_orange_ff7600.png"
                        alt="Fork me on GitHub"></a>
            </el-header>
            <el-main>
                <router-view/>
            </el-main>
        </el-container>
    </div>
</template>

<style lang="scss">
    #app {
        font-family: 'Avenir', Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    #nav {
        padding: 30px;

        a {
            font-weight: bold;
            color: #2c3e50;

            &.router-link-exact-active {
                color: #42b983;
            }
        }
    }

    #plus {
        padding: 0 20px 0 20px;
        display: inline-block;
        font-size: 50px;
        vertical-align: top;
        line-height: 100px;
    }

</style>
