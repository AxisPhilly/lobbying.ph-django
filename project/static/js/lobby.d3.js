if (typeof lobby === 'undefined' || !lobby) {
    var lobby = {};
}

// Helper functions for d3 visualizations
lobby.d3 = {
    showTooltip: function(d) {
        var contents = lobby.d3.createTooltipContent(d);

        if($('.tooltip').length) {
            $('.tooltip').html(contents).show();
        } else {
          $('<div/>', {
            'class': 'tooltip',
            html: contents
          }).appendTo('#graph').show();
        }

        var offset = $('#graph').offset();

        $(document).mousemove(function(e){
             $('.tooltip').css({
                left: e.pageX - offset.left + 90,
                // We have to dynamically set the pageY because the SVG canvas
                // size is dynamic
                top: e.pageY - offset.top + (Math.log(lobby.d3.force.size()[1]) * 41)
            });
        });
    },

    hideTooltip: function() {
        $('.tooltip').hide();
        $(document).unbind('mousemove');
    },

    createTooltipContent: function(d) {
        if (d.type === 'official') {
            return _.template(
                "<p><%= first_name %> <%= last_name %></p>" +
                "<p><%= title %></p>", d);
        } else {
            return d.name;
        }
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
            if (d.position === 2) {
                return 'node oppose';
            } else {
                return 'node support';
            }
        } else if (d.type === 'official') {
            return 'node official ' + d.agency;
        }
    },

    // Checks that the node is within the set x bounds.
    // If it's outside of the bounds, node.x is set
    // to the bound value.
    // Called on each tick for principal nodes.
    // node.position is a reference to the principals
    // position on an issue, ex. support.
    checkBounds: function(node) {
        if (node.x < lobby.d3.bounds[node.position][0]) {
            return lobby.d3.bounds[node.position][0];
        } else if (node.x > lobby.d3.bounds[node.position][1]) {
            return lobby.d3.bounds[node.position][1];
        } else {
            return node.x;
        }
    }
};