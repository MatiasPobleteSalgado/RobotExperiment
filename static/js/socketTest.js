function Search(appl){
	// Constructor
	var _this = this;
	this.app = appl;
	this.form = $("#searchForm");
	this.list = $("#resultList");
	var url = 'http://' + document.domain + ":" +  location.port;
	console.log(url);
	var socket = io.connect(url + "/sock");
	console.log(socket);
	socket.on("msg", function(data){
		console.log( data);
	});
	return this;
}

app.addComponent(Search);
