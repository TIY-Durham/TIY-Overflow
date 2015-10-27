var gulp = require('gulp'),
    inject = require('gulp-inject'),
    sass = require('gulp-sass'),
    wiredep = require('wiredep').stream,
    browserSync = require('browser-sync').create(),
    bower = require('main-bower-files'),
    del = require('del')
; // END var

// see: https://github.com/dlmanning/gulp-sass
gulp.task('sass', function(){
  return gulp.src('src/scss/*.scss')
    .pipe(sass().on('error', sass.logError))
    .pipe(gulp.dest('src/css'))
    .pipe(browserSync.stream())
  ;
});

// see: https://github.com/klei/gulp-inject
gulp.task('inject', [ 'sass' ], function(){
  return gulp.src('./src/*.html', { })
    .pipe(inject(gulp.src([
      './src/**/*.css', './src/**/*.js'
    ], { read: false }), { relative: true }))
    .pipe(gulp.dest('./src'));
});

// see: https://github.com/taptapship/wiredep#gulpjs
gulp.task('wiredep', function(){
  return gulp.src([ './src/*.html', './src/main.scss' ])
    .pipe(wiredep())
    .pipe(gulp.dest('./src'));
});

// see: http://www.browsersync.io/docs/gulp/
gulp.task('serve', [ 'inject', 'sass' ], function(){
  browserSync.init({
    server: {
      baseDir: './src',
      routes: {
        '/bower_components': 'bower_components',
        '/apis': 'apis'
      },
      middleware: function(request, response, next){
        console.log('Hello from middleware!');
        // TODO: Check if `request.method` is `POST` and write something to `response`...?

        next(); // Don't forget this!
      }
    }
  }); // END browserSync.init

  // Re-inject and reload when new `bower_components` are added...
  gulp.watch('bower.json', [ 'wiredep' ])
    .on('change', browserSync.reload);

  gulp.watch('src/scss/*.scss', [ 'sass' ]);

  gulp.watch([ 'src/*.index', 'src/css/main.css', 'src/js/**/*.js' ])
    .on('change', browserSync.reload);
});

gulp.task('build', [ 'inject', 'sass' ], function(){
  // see: https://github.com/sindresorhus/del
  del([ './dist/**', '!./dist' ]).then(function(){
    gulp.src([
      './src/*.html',
      './src/partials/*.html',
      'src/css/*.css',
      'src/js/**/*.js',
    ], { base: 'src' })

      // see: https://github.com/ck86/main-bower-files
      .pipe(gulp.src(bower(), { base: '.' }))

    .pipe(gulp.dest('./dist'));
  });
});

gulp.task('serve:dist', [ 'build' ], function(){
  browserSync.init({
    server: {
      baseDir: './dist'
    }
  });
});
