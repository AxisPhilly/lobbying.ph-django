if (typeof lobby === 'undefined' || !lobby) {
  var lobby = {};
}

lobby.list = {
  getPage: function() {
    var page = 0;

    if (window.location.hash) {
     page = (window.location.hash.replace(/#/,'') - 1);
    }

    return page;
  },
}