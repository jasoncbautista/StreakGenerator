(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;


  var {{replace_class}}VC = function(options){
      var self = this;
      self._delegates = [];
      self._view = new BB.{{replace_MorW}}.{{replace_class}}View();
      self._model = new BB.{{replace_MorW}}.{{replace_class}}Model();
  };

  _.extend({{replace_class}}VC.prototype, {

      getView: function() {
          var self = this;
          return self._view;
      },

      ddfkdsjfsdj: null
  });

  BB.{{replace_MorW}}.{{replace_class}}VC = {{replace_class}}VC;
})(Streak);

/////--------- OR STATIC VERSION -------------------------------------


(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;

  var {{replace_class}}VC = {};

  _.extend({{replace_class}}VC, {

      _initialized: false,

      init: function(cb){
          var self = this;

          if (!self._initialized) {
              self._initialized = true;
              self._delegates = [];
              // Boxes Button
              self._view = new BB.{{replace_MorW}}.{{replace_class}}View();
              self._model = new BB.{{replace_MorW}}.{{replace_class}}Model();
          }

          if (cb) {
              cb();
          }

      },
      dsfdsfsdfsfdsfsfs: null
  });


  BB.{{replace_MorW}}.{{replace_class}}VC = {{replace_class}}VC;

  BB.ready(function(readyCB) {
        {{replace_class}}VC.init(readyCB);
  });


})(Streak);


