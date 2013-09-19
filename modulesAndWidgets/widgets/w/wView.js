(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;


  var wView = function(options){
      var self = this;
      self._delegates = [];
      self._el;
  };

  _.extend(wView.prototype, {

      getEl: function() {
          var self = this;
          return self._el
      },

      ddfkdsjfsdj: null
  });

  BB.Modules.wView = wView;
})(Streak);
