if (typeof lobby === 'undefined' || !lobby) {
    var lobby = {};
}

lobby.d3 = {
    showTooltip: function(d) {
        if($('.tooltip').length) {
            $('.tooltip').html(d.content).show();
        } else {
          $('<div/>', {
            class: 'tooltip',
            html: d.content
          }).appendTo('#graph').show();
        }

        var offset = $('#graph').offset();

        $(document).mousemove(function(e){
             $('.tooltip').css({
                left: e.pageX - offset.left + 90,
                top: e.pageY - offset.top + 160
            });
        });
    },

    hideTooltip: function() {
        $('.tooltip').hide();
        $(document).unbind('mousemove');
    },

    createTooltipContent: function(d) {

    },

    getNodeClass: function(d) {
        if (d.type === 'principal') {
            if (d.position == 2) {
                return 'node oppose';
            } else {
                return 'node support';
            }
        } else if (d.type === 'official') {
            return 'node official ' + d.agency;
        }
    }

};
