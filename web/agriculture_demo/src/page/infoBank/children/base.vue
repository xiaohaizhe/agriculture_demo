<template>
  <div class="three">
     <div id="container" style="height: 700px;"></div>
     <div id="menu">
			<button id="table">TABLE</button>
			<button id="sphere">SPHERE</button>
			<button id="helix">HELIX</button>
      <button id="grid">GRID</button>
		</div>
  </div>
</template>


<script>
  import {get2Data,get3Data} from 'service/getData'

  export default {
    name: 'base',
    data () {
      return {
        camera: null,
        scene: null,
        renderer: null,
        mesh: null,
        controls:null,
        table : [
          "H", "Hydrogen", "1.00794", 1, 1,
          "He", "Helium", "4.002602", 9, 1,
          "Li", "Lithium", "6.941", 1, 2,
          "Be", "Beryllium", "9.012182", 2, 2,
          "B", "Boron", "10.811", 9, 2,
          "C", "Carbon", "12.0107", 8, 2,
          "N", "Nitrogen", "14.0067", 7, 2,
          "O", "Oxygen", "15.9994", 6, 2,
          "F", "Fluorine", "18.9984032", 5, 2,
          "Ne", "Neon", "20.1797", 4, 2,
          "Na", "Sodium", "22.98976...", 1, 3,
          "Mg", "Magnesium", "24.305", 2, 3,
          "Al", "Aluminium", "26.9815386", 3, 3
        ],
        targets : { table: [], sphere: [], helix: [], grid: [] },
        objects : []

      }
    },
    mounted(){
        this.get3Data();

    },
    methods:{
        async get2Data(){
          let resp = await get2Data();
          if(resp.code==0){
            this.table=resp.data;
            this.init();
            this.animate();
          }
        },
        async get3Data(){
          let resp = await get3Data('水稻');
          if(resp.code==0){
            this.table=resp.data;
            this.init();
            this.animate();
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

                // var number = document.createElement( 'div' );
                // number.className = 'number';
                // number.textContent = ( i / 5 ) + 1;
                // element.appendChild( number );

                var symbol = document.createElement( 'div' );
                symbol.className = 'symbol';
                symbol.textContent = this.table[ i ].name;
                element.appendChild( symbol );

                if(this.table[ i ].second_level){
                  var details = document.createElement( 'div' );
                  details.className = 'details';
                  details.textContent = this.table[ i ].second_level + this.table[ i ].first_level;
                  element.appendChild( details );
                }
                

                var object = new THREE.CSS3DObject( element );
                object.position.x = Math.random() * 4000 - 2000;
                object.position.y = Math.random() * 4000 - 2000;
                object.position.z = Math.random() * 4000 - 2000;
                this.scene.add( object );

                this.objects.push( object );

                //

                var object = new THREE.Object3D();
                object.position.x = ( this.table[ i + 1 ] * 220 ) - 1300;
                object.position.y = - ( this.table[ i + 2 ] * 220 ) + 900;

                this.targets.table.push( object );

              }

              // sphere

              var vector = new THREE.Vector3();

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

              var vector = new THREE.Vector3();

              for ( var i = 0, l = this.objects.length; i < l; i ++ ) {

                var theta = i * 0.3 + Math.PI;
                var y = - ( i * 15 ) + 450;

                var object = new THREE.Object3D();

                object.position.setFromCylindricalCoords( 900, theta, y );

                vector.x = object.position.x * 2;
                vector.y = object.position.y;
                vector.z = object.position.z * 2;

                object.lookAt( vector );

                this.targets.helix.push( object );

              }
              // grid

              for ( var i = 0; i < this.objects.length; i ++ ) {

                var object = new THREE.Object3D();

                object.position.x = ( ( i % 3 ) * 250 ) - 800;
                object.position.y = ( - ( Math.floor( i / 3 ) % 3 ) * 250 ) + 800;
                object.position.z = ( Math.floor( i / 9 ) ) * 1000 - 2000;

                this.targets.grid.push( object );

              }

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

                that.transform( that.targets.table, 2000 );

              }, false );

              var button = document.getElementById( 'sphere' );
              button.addEventListener( 'click', function () {

                that.transform( that.targets.sphere, 2000 );

              }, false );

              var button = document.getElementById( 'helix' );
              button.addEventListener( 'click', function () {

                that.transform( that.targets.helix, 2000 );

              }, false );

              var button = document.getElementById( 'grid' );
              button.addEventListener( 'click', function () {

                that.transform( that.targets.grid, 2000 );

              }, false );

              this.transform( this.targets.table, 2000 );
              window.addEventListener( 'resize', this.onWindowResize, false );

              // var elements = document.getElementsByClassName("element");
              // elements.addEventListener( 'click', function(){
              //   alert(1);
              // })
      
          },
          transform:function( targets, duration ) {

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

			#menu {
				position: absolute;
				bottom: 20px;
				width: 100%;
				text-align: center;
			}

			.element {
				width: 200px;
        height: 180px;
        display: flex;
        justify-content: center;
        align-items: center;
				box-shadow: 0px 0px 12px rgba(0,255,255,0.5);
				border: 1px solid rgba(127,255,255,0.25);
				text-align: center;
				cursor: default;
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
					/* position: absolute;
					top: 30px;
					left: 0px;
					right: 0px; */
          font-size: 40px;
          margin: 0 10px;
					/* font-weight: bold; */
					color: rgba(255,255,255,0.75);
					text-shadow: 0 0 0px rgba(0,255,255,0.95);
				}

				.element .details {
					position: absolute;
					bottom: 15px;
					left: 0px;
					right: 0px;
					font-size: 12px;
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