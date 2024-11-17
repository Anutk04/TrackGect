var L = {
    map: function (id, options) {
        return new L.Map(id, options);
    },
    CRS: {
        Simple: {
            scale: function (zoom) {
                return Math.pow(2, zoom);
            }
        }
    },
    imageOverlay: function (url, bounds) {
        return new L.ImageOverlay(url, bounds);
    },
    marker: function (latlng, options) {
        return new L.Marker(latlng, options);
    }
};

// Image overlay
L.ImageOverlay = function (url, bounds) {
    this.url = url;
    this.bounds = bounds;
};

L.ImageOverlay.prototype.addTo = function (map) {
    var img = document.createElement('img');
    img.src = this.url;
    img.style.position = 'absolute';
    map.container.appendChild(img);
};

// Marker functionality
L.Marker = function (latlng, options) {
    this.latlng = latlng;
    this.options = options || {};
};

L.Marker.prototype.addTo = function (map) {
    var markerDiv = document.createElement('div');
    markerDiv.style.position = 'absolute';
    markerDiv.style.left = (this.latlng[1] - 12) + 'px';
    markerDiv.style.top = (this.latlng[0] - 41) + 'px';
    map.container.appendChild(markerDiv);
};