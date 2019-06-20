<template>
  <ul class="predict">
     <li class="mg-bot-20" v-if="this.vegetable.id=='apple'">
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
         <div class="ad-main ad-flex ad-flexBtw">
             <province-chart chartId="priceAnalyse" ref="provinceChart" style="width:35%"></province-chart>
             <div class="avg ad-flex ad-justifyCenter ad-flex ad-flexCol textCenter mg-right-20 mg-left-20">
                <p class="mg-bot-10 textLeft">全国均价：</p>
                <p class="mg-bot-50 textLeft"><span class="ad-blue font-30">{{nationData.value}}</span>元/公斤</p>
                <p class="mg-bot-20 textLeft">同比：<span class="font-bold">{{nationData.year_on_year_rate || 0}}</span></p>
                <p class="textLeft">环比：<span class="font-bold">{{nationData.day_on_day_rate || 0}}</span></p>
             </div>
             <div style="width:40%;overflow:auto;height:300px">
                 <el-table :data="areaData">
                    <el-table-column type="index" label="排名" width="60"></el-table-column>
                    <el-table-column prop="name" label="地区"></el-table-column>
                    <el-table-column prop="value" label="均价(元/公斤)"></el-table-column>
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
         <div class="ad-main ad-flex ad-flexCol"  style="height:450px">
             <ul class="ad-flex ad-end ad-lightgray mg-bot-20">
                 <li class="mg-right-50">更新时间：{{price.updateTime}}</li>
                 <li class="mg-right-50">更新周期：日</li>
                 <li>价格单元：{{price.unit}}</li>
             </ul>
             <div class="ad-lightgray">
                 日期：<el-date-picker
                        v-model="date"
                        type="daterange"
                        @change='dateChange'
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                    <!-- <el-pagination
                        background
                        :current-page="price.currentPage"
                        :page-sizes="[10]"
                        :page-size="10"
                        layout="total, sizes, prev, pager, next"
                        :total="price.total">
                    </el-pagination> -->
                    <el-divider></el-divider>
             </div>
             <div>
                 <el-table :data="priceData" v-if="this.vegetable.id=='apple'">
                    <el-table-column prop="date" label="日期"></el-table-column>
                    <el-table-column prop="variety" label="品种"></el-table-column>
                    <el-table-column prop="province" label="省份"></el-table-column>
                    <el-table-column prop="terminal_market" label="批发市场"></el-table-column>
                    <!-- <el-table-column prop="bottom_price" label="最低价格"></el-table-column>
                    <el-table-column prop="top_price" label="最高价格"></el-table-column> -->
                    <el-table-column prop="average_price" label="平均价格"></el-table-column>
                    <el-table-column prop="measurement_unit" label="计量单位"></el-table-column>
                </el-table>
                <el-table :data="priceData" v-if="this.vegetable.id=='strawberry'">
                    <el-table-column prop="date" label="日期"></el-table-column>
                    <el-table-column prop="name" label="产品"></el-table-column>
                    <el-table-column prop="province" label="省份"></el-table-column>
                    <el-table-column prop="market" label="批发市场"></el-table-column>
                    <el-table-column prop="price" label="价格"></el-table-column>
                    <el-table-column prop="measurement_unit" label="计量单位"></el-table-column>
                </el-table>
             </div>
             
         </div>
      
     </li>
     <li class="mg-bot-20" v-if="this.vegetable.id=='apple'">
        <div class="sub ad-flex ad-flexCenter">
            <div class="cost mg-right-20">
                <i class="ad-icon"></i>
            </div>
            <span class="font-18">成本收益</span>
         </div>
         <div class="ad-main ad-flex ad-flexCol"  style="height:450px">
             <ul class="ad-flex ad-end ad-lightgray mg-bot-20">
                 <li class="mg-right-50">数据来源：农产品成品收益年鉴</li>
                 <li class="mg-right-50">周期：年度</li>
                 <li>更新时间：{{price.updateTime}}</li>
             </ul>
             <!-- <div class="ad-lightgray">
                 日期：<el-date-picker
                        v-model="date"
                        type="daterange"
                        @change='dateChange'
                        range-separator="至"
                        start-placeholder="开始日期"
                        end-placeholder="结束日期">
                    </el-date-picker>
                    <el-divider></el-divider>
             </div> -->
             <div>
                 <el-table :data="fakeData">
                    <el-table-column prop="date" label="日期"></el-table-column>
                    <el-table-column prop="cost" label="现金成本"></el-table-column>
                    <el-table-column prop="profit" label="每亩净利润 (元)"></el-table-column>
                    <!-- <el-table-column prop="variety" label="品种"></el-table-column>
                    <el-table-column prop="province" label="省份"></el-table-column>
                    <el-table-column prop="terminal_market" label="批发市场"></el-table-column>
                    <el-table-column prop="bottom_price" label="最低价格"></el-table-column>
                    <el-table-column prop="top_price" label="最高价格"></el-table-column>
                    <el-table-column prop="average_price" label="平均价格"></el-table-column>
                    <el-table-column prop="measurement_unit" label="计量单位"></el-table-column> -->
                </el-table>
             </div>
             
         </div>
      
     </li>
  </ul>
</template>

<script>
    import {getAppleFuturesData,getApplePriceAnalyse,getStrawPriceAnalyse,getApplePriceDetail,getStrawPriceDetail} from 'service/getData'
    import provinceChart from 'components/charts/provinceChart'
    import {dateFormat} from 'config/mUtils'
    import {mapState} from 'vuex'

    export default {
        name: 'price',
        data () {
            return {
                tableData:[],
                areaData:[],
                nationData:{},
                priceData:[],
                price:{
                    start:'',
                    end:'',
                    updateTime:'',
                    unit:'',
                    currentPage:1,
                    total:0
                },
                date:'',
                //成本收益数据
                fakeData:[{date:'2007/12/31',cost:'无',profit:'2442.57'},
                {date:'2008/12/31',cost:'无',profit:'1945.52'},
                {date:'2009/12/31',cost:'无',profit:'2941.28'},
                {date:'2010/12/31',cost:'无',profit:'5031.68'},
                {date:'2011/12/31',cost:'无',profit:'4611.99'},
                {date:'2012/12/31',cost:'无',profit:'4026.89'},
                {date:'2013/12/31',cost:'无',profit:'3246.72'},
                {date:'2014/12/31',cost:'81.7',profit:'3480.85'},
                {date:'2015/12/31',cost:'75.75',profit:'2128.34'},
                {date:'2016/12/31',cost:'75.83',profit:'896.8'},
                {date:'2017/12/31',cost:'59.53',profit:'无'}]
            }
        },
        mounted(){
            this.price.start = dateFormat(new Date(new Date().getTime() - 14*24*60*60*1000),'',false);
            this.price.end = dateFormat(new Date(),'',false);
            this.date = [this.price.start,this.price.end];
            if(this.vegetable.id=='apple'){
                this.getAppleFuturesData();
                this.getApplePriceAnalyse();
                this.getApplePriceDetail();
            }else{
                this.getStrawPriceAnalyse();
                this.getStrawPriceDetail();
            }
        },
        computed:{
            ...mapState([
                'vegetable'
            ])
        },
        watch:{
            vegetable(curVal,oldVal){
                if(curVal.id=='apple'){
                    this.getAppleFuturesData();
                    this.getApplePriceAnalyse();
                    this.getApplePriceDetail();
                }else{
                    this.getStrawPriceAnalyse();
                    this.getStrawPriceDetail();
                }
    　　　},
        },
        components:{
            'province-chart':provinceChart
        },
        methods:{
            //获取苹果期货最新数据
            async getAppleFuturesData(){
                let resp = await getAppleFuturesData();
                if(resp.code==0){
                    this.tableData = resp.data;
                }
            },
            //获取苹果地区价格行情
            async getApplePriceAnalyse(){
                let resp = await getApplePriceAnalyse();
                if(resp.code==0){
                    this.areaData = resp.data.data;
                    this.nationData = resp.data.nationwide;
                    this.$refs.provinceChart.drawChart(resp.data)
                }
            },
            //获取苹果价格详情列表
            async getApplePriceDetail(){
                let resp = await getApplePriceDetail(this.price.start,this.price.end);
                if(resp.code==0){
                    this.priceData = resp.data;
                    this.price.updateTime = resp.data[0].date;
                    this.price.unit = resp.data[0].measurement_unit;
                    // this.price.total = resp.total_elements;
                }
            },
            //获取草莓地区价格行情
            async getStrawPriceAnalyse(){
                let resp = await getStrawPriceAnalyse();
                if(resp.code==0){
                    this.areaData = resp.data.data;
                    this.nationData = resp.data.nationwide;
                    this.$refs.provinceChart.drawChart(resp.data)
                }
            },
            //获取草莓价格详情列表
            async getStrawPriceDetail(){
                let resp = await getStrawPriceDetail(this.price.start,this.price.end);
                if(resp.code==0){
                    this.priceData = resp.data;
                    this.price.updateTime = resp.data[0].date;
                    this.price.unit = resp.data[0].measurement_unit;
                    // this.price.total = resp.total_elements;
                }
            },
            //日期选择事件
            dateChange(date){
                this.price.start = dateFormat(date[0],'',false);
                this.price.end  = dateFormat(date[1],'',false);
                if(this.$route.params.data=='all' || this.$route.params.data=='apple'){
                    this.getApplePriceDetail();
                }else{
                    this.getStrawPriceDetail();
                }
                
            },
        }
    }
</script>