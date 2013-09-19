(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;


  var BoxesButtonVC = function(options){
      var self = this;
      self._delegates = [];
      self._view = new BB.Modules.BoxesButtonView();
  };

  _.extend(BoxesButtonVC.prototype, {

      getView: function() {
          var self = this;
          return self._view;
      },

      ddfkdsjfsdj: null
  });

  BB.Modules.BoxesButtonVC = BoxesButtonVC;
})(Streak);
