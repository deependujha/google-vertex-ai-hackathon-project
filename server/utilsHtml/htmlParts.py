headingTitle = """
<!DOCTYPE html>
<html>
	<head>
		<meta charset="UTF-8" />
		<title>{businessName}</title>
"""

leftHeading = """
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
		<script src="https://cdn.tailwindcss.com"></script>
		<!-- CSS -->
		<link
			rel="stylesheet"
			href="https://unpkg.com/flickity@2/dist/flickity.min.css"
		/>
		<!-- JavaScript -->
		<script src="https://unpkg.com/flickity@2/dist/flickity.pkgd.min.js"></script>
		<style>
			.gallery {
				background: #eee;
			}

			.gallery-cell {
				width: 66%;
				height: 95vh;
				margin-right: 10px;
				counter-increment: gallery-cell;
			}

			/* cell number */
			.gallery-cell:before {
				display: block;
				text-align: center;
				line-height: 200px;
				font-size: 80px;
				color: white;
			}
		</style>
	</head>
	<body>
"""


navbarColor = """
<!-- navigation bar -->
		<nav class="bg-{color}-500 flex justify-center">
"""

navbarToCarousel = """
			<div class="flex justify-around w-3/5 h-16 items-center">
				<div
					class="text-white text-xl fo font-bold hover:cursor-pointer hover:text-black"
				>
					<a href="#">Home</a>
				</div>
				<div
					class="text-white text-xl font-bold hover:cursor-pointer hover:text-black"
				>
					<a href="#product">Product</a>
				</div>
				<div
					class="text-white text-xl font-bold hover:cursor-pointer hover:text-black"
				>
					<a href="#about">About</a>
				</div>
				<div
					class="text-white text-xl font-bold hover:cursor-pointer hover:text-black"
				>
					<a href="#contact">Contact</a>
				</div>
			</div>
		</nav>
		<main>
			<!-- carousel -->
			<div
				class="gallery js-flickity"
				data-flickity-options='{ "wrapAround": true }'
			>
				<img src="images/carousel/img1.jpeg" class="gallery-cell" alt="" />
				<img src="images/carousel/img2.jpeg" class="gallery-cell" alt="" />
				<img src="images/carousel/img3.jpeg" class="gallery-cell" alt="" />
				<img src="images/carousel/img4.jpeg" class="gallery-cell" alt="" />
			</div>

"""

contactAndCopyRight = """
			<!-- contact us form -->
			<div class="flex flex-col items-center bg-gradient-to-r from-white via-{color}-500 to-white">
				<div
					id="contact"
					class="text-3xl pt-10 text-center font-bold text-white"
				>
					Contact us
				</div>
				<hr style="width: 500px; border: 'solid black 1px'" />
			</div>
			<div class="flex justify-around items-center h-screen bg-gradient-to-r from-white via-{color}-500 to-white">
				<div>
					<div class="flex justify-around" style="width: 90vw">
						<img
							src="images/contact/img4.png"
							style="width: 500px; height: 500px"
							alt="contact"
						/>
						<div
							class="border border-black bg-white rounded-3xl px-5 py-10"
							style="width: 500px"
						>
							<!-- Card content goes here -->
							<div class="mb-4">
								<label
									class="block text-gray-700 text-lg font-bold mb-2"
									for="username"
								>
									Name
								</label>
								<input
									class="shadow appearance-none border rounded text-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
									id="username"
									type="text"
									placeholder="Username"
								/>
							</div>
							<div class="mb-4">
								<label
									class="block text-gray-700 text-lg font-bold mb-2"
									for="email"
								>
									Email
								</label>
								<input
									class="shadow appearance-none border rounded text-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
									id="username"
									type="email"
									placeholder="email"
								/>
							</div>
							<div class="mb-4">
								<label
									class="block text-gray-700 text-lg font-bold mb-2"
									for="msg"
								>
									Message
								</label>
								<textarea
									class="shadow appearance-none border rounded text-lg w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline resize-none"
									id="msg"
									rows="4"
								></textarea>
							</div>
							<div class="mb-4 flex justify-center">
								<button
									class="bg-{color}-500 hover:bg-{color}-700 text-white font-bold py-2 px-4 rounded-full w-full"
								>
									Send message
								</button>
							</div>
						</div>
					</div>
				</div>
			</div>
		</main>
		<!-- footer -->
		<footer class="bg-gray-900 text-gray-100 h-24 flex items-center" id="attr">
			<div class="container mx-auto py-4 px-8">
				<div class="flex flex-wrap justify-between items-center">
					<div class="w-full md:w-auto text-center md:text-left">
						<p>&copy; 2023 Your Company. All rights reserved.</p>
					</div>
					<div class="w-full md:w-auto text-center md:text-right mt-2 md:mt-0">
						<a href="#" class="text-gray-300 hover:text-gray-400 mx-2"
							>Terms of Service</a
						>
						<span class="text-gray-300 mx-2">|</span>
						<a href="#" class="text-gray-300 hover:text-gray-400 mx-2"
							>Privacy Policy</a
						>
					</div>
				</div>
			</div>
		</footer>
	</body>
</html>

"""

productDescription = """
<!-- product description 1 -->
			<div
				class="flex justify-around bg-gradient-to-r from-white to-{color}-500 items-center h-screen"
				id="product"
			>
				<div>
					<div class="flex justify-around" style="width: 90vw">
						<img
							src="images/contact/img4.png"
							style="width: 500px; height: 500px"
							alt="contact"
						/>
						<div class="px-5 self-center" style="max-width: 30vw">
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc1}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc2}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc3}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc4}
							</div>
						</div>
					</div>
				</div>
			</div>

			<!-- product description 2 -->
			<div
				id="about"
				class="flex justify-around bg-gradient-to-r from-{color}-500  items-center h-screen"
			>
				<div>
					<div class="flex justify-around" style="width: 90vw">
						<div class="px-5 self-center" style="max-width: 30vw">
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc5}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc6}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc7}
							</div>
							<div class="text-white text-xl font-bold font-mono py-4">
								{desc8}
							</div>
						</div>
						<img
							src="images/contact/img2.png"
							style="width: 500px; height: 500px"
							alt="contact"
						/>
					</div>
				</div>
			</div>
"""

# print(navbarColor.format(color=colors[3]))
# print(contactAndCopyRight.format(color=colors[3]))
# print(
#     productDescription.format(
#         desc1="my description 1.",
#         desc2="my description 2.",
#         desc3="my description 3.",
#         desc4="my description 4.",
#         desc5="my description 5.",
#         desc6="my description 6.",
#         desc7="my description 7.",
#         desc8="my description 8.",
#     )
# )
