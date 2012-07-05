if (typeof lobby === 'undefined' || !lobby) {
    var lobby = {};
}

// Helper functions for d3 visualizations
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
                top: e.pageY - offset.top + 220
            });
        });
    },

    hideTooltip: function() {
        $('.tooltip').hide();
        $(document).unbind('mousemove');
    },

    createTooltipContent: function(d) {

    },

    // Dynamically set the height based on the number of official nodes
    getHeight: function(nodes) {
        var officials = _.filter(nodes, function(node){
           var type = (node.type === 'official') ? true : false; 
           return type;
        });

        return Math.log(officials.length) * 200;
    },

    getLinkDistance: function(links) {
        return Math.log(links.length) * 85;
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