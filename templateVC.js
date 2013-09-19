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
      self._view = new BB.Modules.{{replace_class}}View();
  };

  _.extend({{replace_class}}VC.prototype, {

      getView: function() {
          var self = this;
          return self._view;
      },

      ddfkdsjfsdj: null
  });

  BB.Modules.{{replace_class}}VC = {{replace_class}}VC;
})(Streak);
