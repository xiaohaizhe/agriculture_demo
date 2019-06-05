<template>
  <div class="three">
     
     <div id="container"></div>
     <div id="menu">
      <button id="choose">重新选择</button>
      <button v-for="(item,index) in btns" :key="item.id" :id="item.id" v-show="level!=4" :class="{active:activeBtn==index}">{{item.name}}</button>
			<!-- <button id="table" v-show="level!=4">表形</button>
			<button id="sphere" v-show="level!=4">球形</button>
			<button id="helix" v-show="level!=4">螺旋形</button> -->
      <!-- <button id="grid">GRID</button> -->
		</div>
    <p class="tip">注：鼠标左键为旋转，鼠标右键为移动</p>
  </div>
</template>


<script>
  import {get2Data,get3Data} from 'service/getData'

  export default {
    name: 'knowledgeBase',
    data () {
      return {
        activeBtn:'0',
        btns:[{
          id:'table',
          name:'表形'
        },{
          id:'sphere',
          name:'球形'
        },{
          id:'helix',
          name:'螺旋形'
        }],
        camera: null,
        scene: null,
        renderer: null,
        mesh: null,
        controls:null,
        table : [],
        secondLevelData:[],
        targets : { table: [], sphere: [], helix: [] },
        objects : [],
        secondSize:0,
        size:0,
        level:2
      }
    },
    mounted(){
        this.get2Data();
    },
    methods:{
        async get2Data(){
          let resp = await get2Data();
          if(resp.code==0){
            this.secondLevelData=resp.data;
            this.table = this.secondLevelData;
            this.secondSize = resp.size;
            this.size = this.secondSize;
            this.level = 2;
            this.init();
            this.animate();
          }
        },
        async get3Data(name){
          let resp = await get3Data(name);
          if(resp.code==0){
            this.table=resp.data;
            this.size = resp.size;
            this.level = 3;
            this.deleteData();
            this.updateData();
          }
        },
        init: function() {
              var that = this; 
              var Three = window.THREE;

              let container = document.getElementById('container');
      
              this.camera = new THREE.PerspectiveCamera( 40, container.clientWidth/container.clientHeight, 1, 10000 );
              this.camera.position.z = 2500;
      
              this.scene = new Three.Scene();


              // table

              for ( var i = 0; i < this.table.length; i += 3 ) {

                var element = document.createElement( 'div' );
                element.className = 'element';
                element.style.backgroundColor = 'rgba(0,127,127,' + ( Math.random() * 0.5 + 0.25 ) + ')';
                element.setAttribute("name", this.table[ i ].name);
                element.onclick = function(){
                  let name = this.getAttribute("name");
                  that.get3Data(name);
                };

                var symbol = document.createElement( 'div' );
                symbol.className = 'symbol';
                symbol.textContent = this.table[ i ].name;
                element.appendChild( symbol );

                if(this.table[ i ].first_level){
                  var second_level = document.createElement( 'div' );
                  second_level.className = 'second_level';
                  second_level.textContent = (this.table[ i ].second_level || "")+this.table[ i ].first_level;
                  element.appendChild( second_level );
                }
                

                var object = new THREE.CSS3DObject( element );
                object.position.x = Math.random() * 4000 - 2000;
                object.position.y = Math.random() * 4000 - 2000;
                object.position.z = Math.random() * 4000 - 2000;
                this.scene.add( object );

                this.objects.push( object );

                //

                var object = new THREE.Object3D();
                object.position.x = ( this.table[ i + 1 ] * 248 ) - 140*this.size;
                object.position.y = - ( this.table[ i + 2 ] * 200 ) + 130*this.size;

                this.targets.table.push( object );

              }

              // sphere

              var vector = new THREE.Vector3(0,0,0);

              for ( var i = 0, l = this.objects.length; i < l; i ++ ) {

                var phi = Math.acos( - 1 + ( 2 * i ) / l );
                var theta = Math.sqrt( l * Math.PI ) * phi;

                var object = new THREE.Object3D();

                object.position.setFromSphericalCoords( 800, phi, theta );

                vector.copy( object.position ).multiplyScalar( 2 );

                object.lookAt( vector );

                this.targets.sphere.push( object );

              }
              // helix

              var vector = new THREE.Vector3(0,0,0);

              for ( var i = 0, l = this.objects.length; i < l; i ++ ) {

                var theta = i * 0.3 + Math.PI;
                var y = - ( i * (this.size*2>12?12:this.size*2) ) + 450;

                var object = new THREE.Object3D();

                object.position.setFromCylindricalCoords( 900, theta, y );

                vector.x = object.position.x * 2;
                vector.y = object.position.y;
                vector.z = object.position.z * 2;

                object.lookAt( vector );

                this.targets.helix.push( object );

              }
              // grid

              // for ( var i = 0; i < this.objects.length; i ++ ) {

              //   var object = new THREE.Object3D();

              //   object.position.x = ( ( i % (this.size/2) ) * 250 ) - 800;
              //   object.position.y = ( - ( Math.floor( i / (this.size/2) ) % (this.size/2) ) * 250 ) + 800;
              //   object.position.z = ( Math.floor( i / ((this.size/2)*(this.size/2)) ) ) * 1000 - 2000;

              //   this.targets.grid.push( object );

              // }

              //

              this.renderer = new THREE.CSS3DRenderer();
              this.renderer.setSize( container.clientWidth, container.clientHeight );
              container.appendChild( this.renderer.domElement );

              //

              this.controls = new THREE.TrackballControls( this.camera, this.renderer.domElement );
              this.controls.rotateSpeed = 0.5;
              this.controls.minDistance = 500;
              this.controls.maxDistance = 6000;
              this.controls.addEventListener( 'change', this.render );


              var button = document.getElementById( 'table' );
              button.addEventListener( 'click', function () {
                that.activeBtn=0;
                that.transform( that.targets.table, 2000 );

              }, false );

              var button = document.getElementById( 'sphere' );
              button.addEventListener( 'click', function () {
                that.activeBtn=1;
                that.transform( that.targets.sphere, 2000 );

              }, false );

              var button = document.getElementById( 'helix' );
              button.addEventListener( 'click', function () {
                that.activeBtn=2;
                that.transform( that.targets.helix, 2000 );

              }, false );

              // var button = document.getElementById( 'grid' );
              // button.addEventListener( 'click', function () {

              //   that.transform( that.targets.grid, 2000 );

              // }, false );

              var choose = document.getElementById( 'choose' );
              choose.addEventListener( 'click', function () {
                //重新选择
                that.activeBtn=0;
                that.table = that.secondLevelData;
                that.size = that.secondSize;
                that.level = 2;
                that.deleteData();
                that.updateData();

              }, false );

              this.transform( this.targets.table, 2000 );
              window.addEventListener( 'resize', this.onWindowResize, false );

              
      
          },
          deleteData(){
             var obj, i;
              for ( i = this.scene.children.length - 1; i >= 0 ; i -- ) {
                  obj = this.scene.children[ i ];
                      this.scene.remove(obj);
              }
              this.targets ={ table: [], sphere: [], helix: []};
              this.objects = [];
          },
          updateData(){
             var that = this;
              // table
              for ( var i = 0; i < this.table.length; i += 3 ) {

                var element = document.createElement( 'div' );
                element.className = 'element';
                element.style.backgroundColor = 'rgba(0,127,127,' + ( Math.random() * 0.5 + 0.25 ) + ')';
                element.setAttribute("name", this.table[ i ].name);
                element.setAttribute("index", i);
                if(this.level===2){
                     element.onclick = function(){
                        let name = this.getAttribute("name");
                        that.activeBtn=0;
                        that.get3Data(name);
                      };
                }else if(this.level===3){
                    element.onclick = function(){
                        that.level=4;
                        that.activeBtn=0;
                        let index = this.getAttribute("index");
                        let html = that.table[ index ].html;
                        that.deleteData();
                        var element = document.createElement( 'div' );
                        element.className = 'element';
                        element.style = 'background-color:rgba(0,127,127,0.3);width: auto;height: auto;color: #fff;'
                        element.innerHTML = html;
                        var object = new THREE.CSS3DObject( element );
                        object.position.x = Math.random() * 4000 - 2000;
                        object.position.y = Math.random() * 4000 - 2000;
                        object.position.z = Math.random() * 4000 - 2000;
                        that.scene.add( object );

                        that.objects.push( object );

                        //

                        var object = new THREE.Object3D();
                        object.position.x = 0;
                        object.position.y = 0;
                        object.position.z = 1500;
                        that.targets.table.push( object );
                        that.transform( that.targets.table, 800 );
                      };
                }

                var symbol = document.createElement( 'div' );
                symbol.className = 'symbol';
                symbol.textContent = this.table[ i ].name;
                element.appendChild( symbol );

                if(this.table[ i ].first_level){
                  debugger
                  var second_level = document.createElement( 'div' );
                  // second_level.className = 'second_level';
                  // second_level.textContent = (this.table[ i ].second_level || "") + '  '+this.table[ i ].first_level;
                  second_level.innerHTML="<p class='second_level'>"+(this.table[ i ].second_level || "")+"</p>"+"<p class='second_level'>"+this.table[ i ].first_level+"</p>";
                  element.appendChild( second_level );
                }
                

                var object = new THREE.CSS3DObject( element );
                object.position.x = Math.random() * 4000 - 2000;
                object.position.y = Math.random() * 4000 - 2000;
                object.position.z = Math.random() * 4000 - 2000;
                this.scene.add( object );

                this.objects.push( object );

                //

                var object = new THREE.Object3D();
                object.position.x = ( this.table[ i + 1 ] * 248 ) - 140*this.size;
                object.position.y = - ( this.table[ i + 2 ] * 200 ) + 130*this.size;

                this.targets.table.push( object );

              }

              // sphere

              var vector = new THREE.Vector3(0,0,0);

              for ( var i = 0, l = this.objects.length; i < l; i ++ ) {

                var phi = Math.acos( - 1 + ( 2 * i ) / l );
                var theta = Math.sqrt( l * Math.PI ) * phi;

                var object = new THREE.Object3D();

                object.position.setFromSphericalCoords( 800, phi, theta );

                vector.copy( object.position ).multiplyScalar( 2 );

                object.lookAt( vector );
                
                this.targets.sphere.push( object );

              }
              // helix

              var vector = new THREE.Vector3(0,0,0);

              for ( var i = 0, l = this.objects.length; i < l; i ++ ) {

                var theta = i * 0.3 + Math.PI;
                var y = - ( i * (this.size*2>12?12:this.size*2) ) + 450;

                var object = new THREE.Object3D();

                object.position.setFromCylindricalCoords( 900, theta, y );

                vector.x = object.position.x * 2;
                vector.y = object.position.y;
                vector.z = object.position.z * 2;

                object.lookAt( vector );

                this.targets.helix.push( object );

              }
              // grid

              // for ( var i = 0; i < this.objects.length; i ++ ) {

              //   var object = new THREE.Object3D();

              //   object.position.x = ( ( i % (this.size/2) ) * 250 ) - 800;
              //   object.position.y = ( - ( Math.floor( i / (this.size/2) ) % (this.size/2) ) * 250 ) + 800;
              //   object.position.z = ( Math.floor( i / ((this.size/2)*(this.size/2)) ) ) * 1000 - 2000;

              //   this.targets.grid.push( object );

              // }
              this.transform( this.targets.table, 2000 );

          },
          transform:function( targets, duration ) {
            this.controls.reset();
            TWEEN.removeAll();

            for ( var i = 0; i < this.objects.length; i ++ ) {

              var object = this.objects[ i ];
              var target = targets[ i ];

              new TWEEN.Tween( object.position )
                .to( { x: target.position.x, y: target.position.y, z: target.position.z }, Math.random() * duration + duration )
                .easing( TWEEN.Easing.Exponential.InOut )
                .start();

              new TWEEN.Tween( object.rotation )
                .to( { x: target.rotation.x, y: target.rotation.y, z: target.rotation.z }, Math.random() * duration + duration )
                .easing( TWEEN.Easing.Exponential.InOut )
                .start();

            }

            new TWEEN.Tween( this )
              .to( {}, duration * 2 )
              .onUpdate( this.render )
              .start();

          },
          onWindowResize:function() {

            this.camera.aspect = container.clientWidth/container.clientHeight;
            this.camera.updateProjectionMatrix();

            this.renderer.setSize( container.clientWidth, container.clientHeight );

            this.render();

          },
          animate: function() { 
              requestAnimationFrame( this.animate );

              TWEEN.update();

              this.controls.update();
          },
          render:function() {

            this.renderer.render( this.scene, this.camera );
          }
    }
  }
</script>
<style>
			.three {
				background-color: #000000;
				margin: 0;
				font-family: Helvetica, sans-serif;;
        overflow: hidden;
        height: 85%;
        position: relative;
			}
      #container{
        height: 100%;
      }
      .tip{
          position: absolute;
          color: #fff;
          text-align: center;
          bottom: 10px;
      }
			a {
				color: #ffffff;
			}

			#info {
				position: absolute;
				width: 100%;
				color: #ffffff;
				padding: 5px;
				font-family: Monospace;
				font-size: 13px;
				font-weight: bold;
				text-align: center;
				z-index: 1;
			}
      #menu .active{
        background-color: rgba(0,255,255,0.5);
      }
			#menu {
				position: absolute;
        bottom: 10px;
        width: 100%;
        /* margin-bottom: 10px; */
				text-align: center;
			}

			.element {
				width: 228px;
        height: 180px;
        display: flex;
        justify-content: center;
        align-items: center;
				box-shadow: 0px 0px 12px rgba(0,255,255,0.5);
				border: 1px solid rgba(127,255,255,0.25);
				text-align: center;
        cursor: default;
        flex-direction: column;
			}

			.element:hover {
				box-shadow: 0px 0px 12px rgba(0,255,255,0.75);
				border: 1px solid rgba(127,255,255,0.75);
			}

      .element .number {
        position: absolute;
        top: 20px;
        right: 20px;
        font-size: 12px;
        color: rgba(127,255,255,0.75);
      }

      .element .symbol {
        margin: 0px 5px;
        font-size: 36px;
        color: rgba(255,255,255,0.75);
        text-shadow: 0 0 0px rgba(0,255,255,0.95);
      }

      .element .second_level {
        margin: 10px;
        font-size: 22px;
        color: rgba(127,255,255,0.75);
      }
      .element .first_level {
        font-size: 20px;
        color: rgba(127,255,255,0.75);
      }

			button {
				color: rgba(127,255,255,0.75);
				background: transparent;
				outline: 1px solid rgba(127,255,255,0.75);
				border: 0px;
				padding: 5px 10px;
				cursor: pointer;
			}
			button:hover {
				background-color: rgba(0,255,255,0.5);
			}
			button:active {
				color: #000000;
				background-color: rgba(0,255,255,0.75);
			}
		</style>