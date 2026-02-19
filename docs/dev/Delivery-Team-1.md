# Delivery Team 1

## Files
- [Everything in a zip file](../FRONT/Delivery-Team-1-group1_blogsbu-zip.md)
- [The HTML file we presented](../FRONT/Delivery-Team-1-presented_version-html.md) (also shown below)
- [Beta version with some additions that didn't work too well](../FRONT/Delivery-Team-1-beta_version-html.md) (also shown below)
- [Stylesheet](../FRONT/Delivery-Team-1-style-css.md)

## The main HTML file we presented
```html
﻿<!doctype html>
<html lang="no">
<head>
	<meta charset="utf-8">
	<title>Blogsbu</title>
	<link rel="stylesheet" href="style.css" media="all" />
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>
	
	<script>
	function getRequestParam(name){
		name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
		var regexS = "[\\?&]"+name+"=([Delivery Team 1^&#]*)";
		var regex = new RegExp( regexS );
		var results = regex.exec( window.location.href );
		if( results == null ) {
			return "";
		} else {
			return results[1];
		}
	}
	
	function drawLogo() {
		var canvas = document.getElementById('logoCanvas');  
		var ctx = canvas.getContext('2d');  
		
		ctx.font = "bold 52px sans-serif";
		ctx.textAlign = "center";
		ctx.textBaseline  = "middle";
		ctx.fillStyle = "#fff";
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.shadowBlur    = 5;
		ctx.shadowColor   = "black";
		ctx.fillText("Blogsbu!", canvas.width / 2, canvas.height / 2);
	}
	</script>
	<script>
		/**
		 * Called when document is ready.
		 */
		$(function() {
			drawLogo();

			var postsContainer = $("section.posts");

			var postsItem = localStorage.getItem("posts");
			if (postsItem) {
				var posts = JSON.parse(postsItem);
				for (var i in posts) {
					postsContainer.append(jsonArticleToDomArticle(posts[i]));
				}
			}

			// hook up controls/actions to existing posts
			$("article.post").each(function() {
				var article = this;
				$("details input.edit", article).click(function() {
					startEditing(article);
				});

				$("details input.delete", article).click(function() {
					deleteArticle(article);
				});
			});
		});

		function domArticleToJsonArticle(article) {
			return {
				date: $("> header time", article).attr("datetime"),
				title: $("> header h2", article).attr("innerHTML"),
				content: $("> section", article).attr("innerHTML")
			};
		}

		function jsonArticleToDomArticle(article) {
			return $(
				'<article class="post">' +
					'<header>' + 
						'<h2>' + article.title + '</h2>' +
						/*
						'Published <time datetime="' + article.date + '"></time>' +
						*/
					'</header>' +
					'<section>' +
						article.content +
					'</section>' +
					'<details>' + 
						'<input type="button" class="edit" value="Edit" />' +
						'<input type="button" class="delete" value="Delete" />' +
					'</details>' + 
				'</article>').get(0);
		}

		function getTitleElement(article) {
			return $("header h2", article).get(0);
		}

		function getContentElement(article) {
			return $("section", article).get(0);
		}

		function startEditing(article) {
			console.log("Start editing");
			var title = getTitleElement(article);
			var content = getContentElement(article);
			title.contentEditable = true;
			content.contentEditable = true;

			// disable edit button
			$("input.edit", article).attr("disabled", true);

			// add save button
			var saveButton = document.createElement("input");
			saveButton.type = "button";
			saveButton.className = "save";
			saveButton.value = "Save";
			saveButton.onclick = function() {
				saveArticle(article);
			};

			$("details input.delete", article).before(saveButton);

			// focus content
			$("section", article).focus();
		}

		function stopEditing(article) {
			console.log("Stop editing");
			getTitleElement(article).contentEditable = false;
			getContentElement(article).contentEditable = false;
		}

		function saveArticle(article) {
			console.log("Save article");
			stopEditing(article);
			$("input.save", article).remove();
			$("input.edit", article).attr("disabled", false);

			var posts = [];
			$("article.post").each(function() {
				posts.push(domArticleToJsonArticle(this));
			});
			localStorage.setItem("posts", JSON.stringify(posts));
		}

		function deleteArticle(article) {
			if (confirm("Are you sure you want to delete the post?")) {
				console.log("Delete article");
				$(article).remove();
				// TODO: remove from local storage
			}
		}

		function newPost() {
			var postContainer = $("section.posts");
			var post = $(
				'<article class="post">' +
					'<header>' + 
						'<h2 contentEditable="true">Title goes here</h2>' +
					'</header>' + 
					'<section contentEditable="true">' + 
						'Lorem ipsum dolor sit amet' +
					'</section>' +
					'<details>' + 
						'<input type="button" class="save" value="Save"/>' +
						'<input type="button" class="cancel" value="Cancel"/>' +
					'</details>' +
				'</article>');

			$("input.save", post).click(function() {
				$("input.cancel", post).remove();

				saveArticle(post.get(0));

				var editButton = $('<input type="button" class="edit" value="Edit" />');
				editButton.click(function () {
					startEditing(post.get(0));
				});

				var deleteButton = $('<input type="button" class="delete" value="Delete" />');
				deleteButton.click(function () {
					deleteArticle(post.get(0));
				});

				$("details", post).append(editButton);
				$("details", post).append(deleteButton);
			});

			$("input.cancel", post).click(function() {
				console.log("Cancel new post");
				post.remove();
			});

			postContainer.prepend(post);
			$("header h2", post).focus();
		}
	</script>
</head>
<body>
	<nav>
		<ul>
			<li><a href="#">Home</a></li>
			<li><a href="#">Most popular</a></li>
			<li><a href="#">Mentions</a></li>
			<li><a href="#">September</a></li>
			<li><a href="#">August</a></li>
			<li><a href="#">July</a></li>
			<li><a href="#">Older</a></li>
		</ul>
	</nav>

	<section role="main">
		<header>
			<canvas id="logoCanvas" width="400" height="80"></canvas>
		</header>
		<section class="controls">
			<input type="button" value="New post" onclick="newPost()" />
		</section>
		<section class="posts">
		</section>
	</section>
	
	<footer>Blogsbu &copy; 2010</footer>
</body>
</html>
```

## A beta version with some additional features that didn't work too well
```html
﻿<!doctype html>
<html lang="no">
<head>
	<meta charset="utf-8">
	<title>Blogsbu</title>
	<link rel="stylesheet" href="style.css" media="all" />
	<script src="http://ajax.googleapis.com/ajax/libs/jquery/1.4.3/jquery.min.js"></script>
	
	<script>
	function getRequestParam(name){
		name = name.replace(/[\[]/,"\\\[").replace(/[\]]/,"\\\]");
		var regexS = "[\\?&]"+name+"=([Delivery Team 1^&#]*)";
		var regex = new RegExp( regexS );
		var results = regex.exec( window.location.href );
		if( results == null ) {
			return "";
		} else {
			return results[1];
		}
	}
	
	function drawLogo() {
		var canvas = document.getElementById('logoCanvas');  
		var ctx = canvas.getContext('2d');  
		
		ctx.font = "bold 52px sans-serif";
		ctx.textAlign = "center";
		ctx.textBaseline  = "middle";
		ctx.fillStyle = "#fff";
		ctx.shadowOffsetX = 0;
		ctx.shadowOffsetY = 0;
		ctx.shadowBlur    = 5;
		ctx.shadowColor   = "black";
		ctx.fillText("Blogsbu!", canvas.width / 2, canvas.height / 2);
	}
	</script>
	<script>
		/**
		 * Called when document is ready.
		 */
		$(function() {
			drawLogo();

			var postsContainer = $("section.posts");

			var postsItem = localStorage.getItem("posts");
			if (postsItem) {
				var posts = JSON.parse(postsItem);
				for (var i in posts) {
					postsContainer.append(jsonArticleToDomArticle(posts[i]));
				}
			}

			// hook up controls/actions to existing posts
			$("article.post").each(function() {
				var article = this;
				$("details input.edit", article).click(function() {
					startEditing(article);
				});

				$("details input.delete", article).click(function() {
					deleteArticle(article);
				});
			});
		});

		function domArticleToJsonArticle(article) {
			return {
				date: $("> header time", article).attr("datetime"),
				title: $("> header h2", article).attr("innerHTML"),
				content: $("> section", article).attr("innerHTML")
			};
		}

		function jsonArticleToDomArticle(article) {
			return $(
				'<article class="post">' +
					'<header>' + 
						'<h2>' + article.title + '</h2>' +
						/*
						'Published <time datetime="' + article.date + '"></time>' +
						*/
					'</header>' +
					'<section>' +
						article.content +
					'</section>' +
					'<details>' + 
						'<input type="button" class="edit" value="Edit" />' +
						'<input type="button" class="delete" value="Delete" />' +
					'</details>' + 
				'</article>').get(0);
		}

		function getTitleElement(article) {
			return $("header h2", article).get(0);
		}

		function getContentElement(article) {
			return $("section", article).get(0);
		}

		function startEditing(article) {
			console.log("Start editing");
			var title = getTitleElement(article);
			var content = getContentElement(article);
			title.contentEditable = true;
			content.contentEditable = true;

			// disable edit button
			$("input.edit", article).attr("disabled", true);

			// add save button
			var saveButton = document.createElement("input");
			saveButton.type = "button";
			saveButton.className = "save";
			saveButton.value = "Save";
			saveButton.onclick = function() {
				saveArticle(article);
			};

			$("details input.delete", article).before(saveButton);

			// focus content
			$("section", article).focus();
		}

		function stopEditing(article) {
			console.log("Stop editing");
			getTitleElement(article).contentEditable = false;
			getContentElement(article).contentEditable = false;
		}

		function saveArticle(article) {
			console.log("Save article");
			stopEditing(article);
			$("input.save", article).remove();
			$("input.edit", article).attr("disabled", false);

			var posts = [];
			$("article.post").each(function() {
				posts.push(domArticleToJsonArticle(this));
			});
			localStorage.setItem("posts", JSON.stringify(posts));
		}

		function deleteArticle(article) {
			if (confirm("Are you sure you want to delete the post?")) {
				console.log("Delete article");
				$(article).remove();
				// TODO: remove from local storage
			}
		}

		function newPost() {
			var postContainer = $("section.posts");
			var post = $(
				'<article class="post">' +
					'<header>' + 
						'<h2 contentEditable="true">Title goes here</h2>' +
					'</header>' + 
					'<section contentEditable="true">' + 
						'Lorem ipsum dolor sit amet' +
					'</section>' +
					'<details>' + 
						'<input type="button" class="save" value="Save"/>' +
						'<input type="button" class="cancel" value="Cancel"/>' +
					'</details>' +
				'</article>');

			$("input.save", post).click(function() {
				$("input.cancel", post).remove();

				saveArticle(post.get(0));

				var editButton = $('<input type="button" class="edit" value="Edit" />');
				editButton.click(function () {
					startEditing(post.get(0));
				});

				var deleteButton = $('<input type="button" class="delete" value="Delete" />');
				deleteButton.click(function () {
					deleteArticle(post.get(0));
				});

				$("details", post).append(editButton);
				$("details", post).append(deleteButton);
			});

			$("input.cancel", post).click(function() {
				console.log("Cancel new post");
				post.remove();
			});

			postContainer.prepend(post);
			$("header h2", post).focus();
		}
	</script>
</head>
<body>
	<nav>
		<ul>
			<li><a href="#">Home</a></li>
			<li><a href="#">Most popular</a></li>
			<li><a href="#">Mentions</a></li>
			<li><a href="#">September</a></li>
			<li><a href="#">August</a></li>
			<li><a href="#">July</a></li>
			<li><a href="#">Older</a></li>
		</ul>
	</nav>

	<section role="main">
		<header>
			<canvas id="logoCanvas" width="400" height="80"></canvas>
		</header>
		<section class="controls">
			<input type="button" value="New post" onclick="newPost()" />
		</section>
		<section class="posts">
		</section>
	</section>
	
	<footer>Blogsbu &copy; 2010</footer>
</body>
</html>
```
