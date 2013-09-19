(function(Streak) {
  var $ = Streak.jQuery,
    Gmail = Streak.Gmail,
    BB = Streak.BentoBox,
    HTML = Streak.HTML,
    Locale = Streak.Locale,
    _ = Streak._,
    Date = Streak.Date;


  var {{replace_class}}View = function(options){
      var self = this;
      self._delegates = [];
      self._el;
  };

  _.extend({{replace_class}}View.prototype, {

      getEl: function() {
          var self = this;
          return self._el
      },

      ddfkdsjfsdj: null
  });

  BB.{{replace_MorW}}.{{replace_class}}View = {{replace_class}}View;
})(Streak);
