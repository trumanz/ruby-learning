'use strict';

module.exports = function(grunt) {
  grunt.initConfig({
    concat_sourcemap: {
      options: {
        sourcesContent: true
      },
      target: {
        files: {
          'dist/jsongui.js': [

            // License & version info, start the containing closure
            'src/intro.js',
            'src/jsongui.js',
            'src/menu/menu.js',
            'src/editor/editor.js',
            'src/jtree_json.js'
          ],
        }
      }
    },
    uglify: {
      dist: {
        src: 'dist/jsongui.js',
        dest: 'dist/jsongui.min.js'
      },
      options: {
        preserveComments: 'some'
      }
    },
    watch: {
      scripts: {
        files: ["src/**/*.js", "Gruntfile.js"],
        tasks: ["concat_sourcemap"]
      }
    },
    jshint: {
      options: {
        browser: true,
        indent: 2,
        nonbsp: true,
        nonew: true,
        immed: true,
        latedef: true
      },
      beforeconcat: [
         
      ],
      afterconcat: {
        options: {
          undef: true
        },
        files: {
          src: ['dist/jsoneditor.js']
        }
      }
    }
  });

  // These plugins provide necessary tasks.
  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-concat-sourcemap');

  // Default task.
  grunt.registerTask('default', ['jshint:beforeconcat','concat_sourcemap','jshint:afterconcat','uglify']);

};
