<template>
  <ul class="predict forecast">
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="forecast mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">价格预测</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw" style="width:100%">
             <forecast-chart chartId="forecast" ref="forecastChart" style="width:100%"></forecast-chart>
         </div>
      </li>
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="price mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">价格概率</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw" style="width:100%">
             <!-- <price-chart chartId="price" ref="priceChart" style="width:100%"></price-chart> -->
         </div>
      </li>
      <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="risk mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">风险预警模型</span>
         </div>
         <div class="ad-main ad-flex ad-flexBtw" style="width:100%">
             <!-- <risk-chart chartId="risk" ref="riskChart" style="width:100%"></risk-chart> -->
         </div>
      </li>
  </ul>
</template>

<script>
  import forecastChart from 'components/charts/forecastChart'
  // import priceChart from 'components/charts/priceChart'
  // import riskChart from 'components/charts/riskChart'

  export default {
    name: 'forecast',
    data () {
      return {
      }
    },
    components:{
        'forecast-chart':forecastChart,
        // 'price-chart':priceChart,
        // 'risk-chart':riskChart
    },
    mounted(){
      this.$refs.forecastChart.drawChart();
    }
  }
</script>
