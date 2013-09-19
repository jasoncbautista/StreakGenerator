(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;


  var BoxesButtonView = function(options){
      var self = this;
      self._delegates = [];
      self._el;
  };

  _.extend(BoxesButtonView.prototype, {

      getEl: function() {
          var self = this;
          return self._el
      },

      ddfkdsjfsdj: null
  });

  BB.Modules.BoxesButtonView = BoxesButtonView;
})(Streak);
