var gulp = require( 'gulp' ),
    clean = require( 'gulp-clean' ),
    jspm = require( 'gulp-jspm' ),
    sass = require( 'gulp-sass' ),
    csso = require('gulp-csso'),
    uglify = require( 'gulp-uglify' ),
    sourcemaps = require( 'gulp-sourcemaps' ),
    livereload = require( 'gulp-livereload' );

var env = require( './env.js' );

gulp.task( 'assemble', [ 'assemble:markup', 'assemble:scripts', 'assemble:styles', 'assemble:images', 'assemble:fonts' ] );

gulp.task( 'assemble:markup', function(){
  gulp.src( env.markup.src_files )
      .pipe( livereload() )
      .pipe( gulp.dest( env.markup.dest ) );
} );

gulp.task( 'assemble:scripts', function(){
  gulp.src( env.scripts.src + 'main.js' )
      .pipe( sourcemaps.init() )
      .pipe( jspm( { selfExecutingBundle: true } ) )
      .pipe( uglify() )
      .pipe( sourcemaps.write( '.' )  )
      .pipe( livereload() )
      .pipe( gulp.dest( env.scripts.dest ) );
} );

gulp.task( 'assemble:styles', function(){
  return  gulp.src( env.styles.src + 'main.scss' )
      				.pipe( sourcemaps.init() )
      				.pipe( sass() )
              .pipe( csso() )
      				.pipe( sourcemaps.write( '.' ) )
              .pipe( livereload() )
      				.pipe( gulp.dest( env.styles.dest ) );
} );

gulp.task( 'assemble:images', function(){
  return  gulp.src( env.images.src_files )
              .pipe( gulp.dest( env.images.dest ) );
} );

gulp.task( 'assemble:fonts', function(){
  return  gulp.src( env.fonts.src_files )
              .pipe( gulp.dest( env.fonts.dest ) );
} );

gulp.task( 'watch', function(){
  livereload.listen();
  gulp.watch( env.markup.src_files, [ 'assemble:markup' ] );
  gulp.watch( env.styles.src_files, [ 'assemble:styles' ] );
  gulp.watch( env.scripts.src_files, [ 'assemble:scripts' ] );
} );

gulp.task( 'clean', function(){
	return 	gulp.src( [ env.static, env.templates ], { read: false } )
				      .pipe( clean( { force : true } ) );
} );

gulp.task( 'default', [ 'clean' ], function(){
  gulp.start( 'assemble' );
  gulp.start( 'watch' );
} );
