<template>
  <ul class="predict">
     <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="finance mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">金融市场行情</span>
         </div>
         <div class="ad-main">
            <el-table :data="tableData">
                <el-table-column prop="variety_month" label="品种月份"></el-table-column>
                <el-table-column prop="date" label="时间"></el-table-column>
                <el-table-column prop="settlement_price_yesterday" label="昨结算"></el-table-column>
                <el-table-column prop="opening_price" label="今开盘"></el-table-column>
                <el-table-column prop="top_price" label="最高价"></el-table-column>
                <el-table-column prop="bottom_price" label="最低价"></el-table-column>
                <el-table-column prop="closing_price" label="今收盘"></el-table-column>
                <el-table-column prop="settlement_price_today" label="今结算"></el-table-column>
                <el-table-column prop="up" label="涨跌1">
                    <template slot-scope="scope">
                        {{scope.row.closing_price-scope.row.settlement_price_yesterday}}
                    </template>
                </el-table-column>
                <el-table-column prop="down" label="涨跌2">
                    <template slot-scope="scope">
                        {{scope.row.settlement_price_today-scope.row.settlement_price_yesterday}}
                    </template>
                </el-table-column>
                <el-table-column prop="number_of_transactions" label="成交量(手)"></el-table-column>
                <el-table-column prop="open_interest" label="空盘量">
                </el-table-column>
                <!-- <el-table-column prop="id" label="增减量"></el-table-column> -->
                <el-table-column prop="turnover" label="成交额(万元)"></el-table-column>
                <!-- <el-table-column prop="id" label="交割结算价"></el-table-column> -->
            </el-table>
         </div>
     </li>
     <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="map mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">地区行情</span>
         </div>
         <div class="ad-main ad-flex">
             <province-chart chartId="priceAnalyse" ref="provinceChart" style="width:33%"></province-chart>
             <div class="avg ad-flex ad-justifyCenter ad-flex ad-flexCol textCenter mg-right-20 mg-left-20">
                <p class="mg-bot-10">全国均价：</p>
                <p class="mg-bot-50"><span class="ad-blue font-30">23.3</span>元/公斤</p>
                <p class="mg-bot-20">同比：<span class="font-bold">20%</span></p>
                <p>环比：<span class="font-bold">20%</span></p>
             </div>
             <div style="width:33%">
                 <el-table :data="areaData">
                    <el-table-column prop="variety_month" label="排名"></el-table-column>
                    <el-table-column prop="province" label="地区"></el-table-column>
                    <el-table-column prop="average_latest" label="均价(元/公斤)"></el-table-column>
                    <el-table-column prop="day_on_day_rate" label="环比"></el-table-column>
                    <el-table-column prop="year_on_year_rate" label="同比"></el-table-column>
                </el-table>
             </div>
         </div>
      
     </li>
     <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="market mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">市场价格</span>
         </div>
         <div class="ad-main ad-flex">
         </div>
      
     </li>
     <li class="mg-bot-20">
        <div class="sub ad-flex ad-flexCenter">
            <div class="cost mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">成本收益</span>
         </div>
         <div class="ad-main ad-flex">
         </div>
      
     </li>
  </ul>
</template>

<script>
    import {getAppleFuturesData,getPriceAnalyse} from 'service/getData'
    import provinceChart from 'components/charts/provinceChart'

    export default {
        name: 'price',
        data () {
            return {
                tableData:[],
                areaData:[]
            }
        },
        mounted(){
            // this.getAppleFuturesData();
            // this.getPriceAnalyse();
        },
        components:{
            'province-chart':provinceChart
        },
        methods:{
            async getAppleFuturesData(){
                let resp = await getAppleFuturesData();
                if(resp.code==0){
                    this.tableData = resp.data;
                }
            },
            async getPriceAnalyse(){
                let resp = await getPriceAnalyse();
                if(resp.code==0){
                    this.areaData = resp.data;
                    this.$refs.provinceChart.drawChart(resp.data)
                }
            },
        }
    }
</script>