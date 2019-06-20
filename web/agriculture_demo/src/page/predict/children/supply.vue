<template>
  <ul class="predict supply">
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="output mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">产量及种植面积</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw" style="width:100%">
             <output-chart chartId="output" ref="outputChart" style="width:100%"></output-chart>
         </div>
      </li>
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="product mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">产区及各主产省产量</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw">
            <product-chart chartId="product" ref="productChart" style="width:100%"></product-chart>
         </div>
      </li>
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="consume mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">消费情况</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw">
            <consume-chart chartId="consume" ref="consumeChart" style="width:100%"></consume-chart>
         </div>
      </li>
      <!-- <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="storage mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">库容分布（没有数据）</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw">
            <storage-chart chartId="storage" ref="storageChart" style="width:100%"></storage-chart>
         </div>
      </li> -->
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="import mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">进出口情况</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw">
            <import-chart chartId="import" ref="importChart" style="width:100%"></import-chart>
         </div>
      </li>
  </ul>
</template>

<script>
    import outputChart from 'components/charts/outputChart'
    import consumeChart from 'components/charts/consumeChart'
    // import storageChart from 'components/charts/storageChart'
    import importChart from 'components/charts/importChart'
    import productChart from 'components/charts/productChart'
    import {mapState} from 'vuex'

    export default {
        name: 'supply',
        data () {
        return {
            }
        },
        computed:{
            ...mapState([
                'vegetable'
            ])
        },
        components:{
            'output-chart':outputChart,
            'consume-chart':consumeChart,
            // 'storage-chart':storageChart,
            'import-chart':importChart,
            'product-chart':productChart
        },
        watch:{
            vegetable(curVal,oldVal){
                this.$refs.outputChart.drawChart(curVal.id);
                this.$refs.productChart.drawChart(curVal.id);
                this.$refs.consumeChart.drawChart(curVal.id);
                // this.$refs.storageChart.drawChart(curVal.id);
                this.$refs.importChart.drawChart(curVal.id);
    　　　},
        },
        mounted(){
            this.$refs.outputChart.drawChart(this.vegetable.id);
            this.$refs.productChart.drawChart(this.vegetable.id);
            this.$refs.consumeChart.drawChart(this.vegetable.id);
            // this.$refs.storageChart.drawChart(this.vegetable.id);
            this.$refs.importChart.drawChart(this.vegetable.id);
        },
        methods:{

        }
    }
</script>
