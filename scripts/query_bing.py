import os
import time
from urllib import request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE_URL = "https://www.bing.com/create?toWww=1&redig=30C04FC20A7A4BA08168CC7BB17EDFD6"
SAVE_PATH = "C:/dev/personal/ecom/next_DBC/scripts/public"
CHROME_DRIVER_PATH = "C:/path/to/chromedriver.exe"


landscape = [    "Generate a list of 10 native plants that thrive in your local climate and provide a visual guide on how to incorporate them into a landscape design.",    "Create an article discussing the benefits of sustainable landscaping practices, including water conservation, energy efficiency, and reduced maintenance costs.",    "Develop a step-by-step guide to creating a DIY garden using recycled materials and inexpensive plantings.",    "Design a visually stunning landscape that incorporates natural elements such as rocks, trees, and water features.",    "Write a blog post about the importance of seasonal maintenance, including pruning, fertilization, and pest control.",    "Create a video tutorial on how to install a drip irrigation system to minimize water waste and reduce overall maintenance.",    "Develop a guide to the best mulching practices for your region, including how to choose the right type of mulch and how to apply it effectively.",    "Write a detailed article on how to create a low-maintenance lawn that requires minimal watering and mowing.",    "Create a social media campaign showcasing before-and-after photos of recent landscaping projects, highlighting the impact of professional design and installation.",    "Develop a series of infographics illustrating the benefits of incorporating different types of plants into a landscape design, including increased biodiversity, improved air quality, and reduced erosion."]
Dynamic_Website_Art = [    "Create a dynamic background image for the website header with a space theme.",    "Generate a beautiful animated logo for the website using a dragonfly.",    "Produce a visually stunning 3D animation of a flock of birds flying across the screen.",    "Design a beautiful and creative loading screen for the website.",    "Generate a unique and eye-catching icon for the website's bookmark.",    "Create a beautiful and minimalist navigation menu with icons.",    "Produce an interactive image gallery with images of nature.",    "Design a beautiful and dynamic background video for the website.",    "Generate a visually striking background pattern with geometric shapes.",    "Produce a beautiful and unique illustration of the website's mascot.",    "Create a dynamic and interactive timeline of the website's history.",    "Generate a beautiful and animated countdown timer for the website's upcoming event.",    "Design a creative and dynamic footer with a scrolling effect.",    "Produce a visually stunning carousel of images with different effects.",    "Create a beautiful and interactive map of the website's location.",    "Generate a visually striking hero image with a parallax effect.",    "Design a beautiful and unique infographic with data visualization.",    "Produce a dynamic and interactive quiz with different question types.",    "Create a visually stunning 404 error page with a fun message.",    "Generate a beautiful and interactive contact form with animation effects."]
simple_tattoo = [    "A tiny unicorn tattooed on the wrist, surrounded by stars.",    "A small fairy tattoo on the back of the neck with butterfly wings.",    "A heart-shaped tattoo with angel wings and a halo above it.",    "A tiny mermaid tattoo on the ankle with a seashell crown.",    "A magical potion bottle tattoo with sparkles and glitter.",    "A small dragonfly tattoo on the collarbone with iridescent wings.",    "A cute fox tattoo on the arm with a flower crown.",    "A tiny crescent moon tattoo on the finger with stars.",    "A small butterfly tattoo on the wrist with watercolor effect.",    "A unicorn horn tattoo on the forearm with a rainbow trail.",    "A magical wand tattoo on the hand with stars and sparkles.",    "A small bee tattoo on the ankle with honeycomb and flowers.",    "A tiny mushroom tattoo on the back of the ear with tiny fairies.",    "A cute panda tattoo on the shoulder with a bamboo shoot.",    "A small crescent moon and star tattoo on the ankle.",    "A small hummingbird tattoo on the wrist with watercolor effect.",    "A magical key tattoo on the back of the neck with glitter.",    "A cute owl tattoo on the shoulder with a moon in the background.",    "A small heart tattoo on the finger with an arrow through it.",    "A tiny lightning bolt tattoo on the wrist with a storm cloud."]

MM = [
    "Write a short story about a person who discovers the benefits of magic mushrooms and decides to start a business selling them.",
    "Create a series of social media posts promoting the different types of magic mushrooms sold by the company.",
    "Write an informative blog post about the history and cultural significance of magic mushrooms.",
    "Design a logo for the magic mushroom company that incorporates the unique qualities of the mushrooms they sell.",
    "Create a list of delicious recipes that feature magic mushrooms as a key ingredient.",
    "Write an article about the scientific research behind the benefits of magic mushrooms for mental health.",
    "Develop a marketing strategy to reach new customers who are interested in natural remedies and holistic health practices.",
    "Create a video that showcases the beauty and diversity of the magic mushrooms grown and sold by the company.",
    "Write a how-to guide for growing magic mushrooms at home, with tips and tricks for success.",
    "Develop an educational program for schools and community groups that teaches the benefits and potential risks of magic mushrooms."
]

Freel = [
  "Create an image of a couple standing on a hilltop with a beautiful sunset in the background, holding hands and smiling.",
         "Generate a photo of a baby giggling while playing with a set of colorful toys.",
         "Design a picture of a family gathered around a campfire at night, roasting marshmallows and telling stories.",
         "Create an image of a bride and groom exchanging vows in a beautiful outdoor wedding ceremony.",
         "Generate a photo of a group of friends laughing and having fun on a beach vacation.",
         "Design a picture of a stunning landscape with a waterfall cascading down a rocky cliff.",
         "Create an image of a musician performing on stage in front of a cheering crowd.",
         "Generate a photo of a woman looking out at a beautiful city skyline at night.",
         "Design a picture of a group of people enjoying a picnic in a park on a sunny day.",
         "Create an image of a person hiking up a mountain trail, surrounded by beautiful scenery.",
         "Generate a photo of a child blowing out birthday candles on a cake surrounded by family and friends.",
         "Design a picture of a couple enjoying a romantic dinner in a candlelit restaurant.",
         "Create an image of a person sitting on a bench, reading a book in a peaceful garden.",
         "Generate a photo of a group of people gathered around a table, playing a board game.",
    "Design a picture of a woman relaxing in a hammock, surrounded by trees and a beautiful"
]



magical_products = [
    "Enchanted Crystal Forest",
    "Mystical Aurora Skyscraper",
    "Wizard's Potion Laboratory",
    "Magical Cybernetic Animals",
    "Ethereal Dreamcatcher Office",
    "Moonlit Dragon Boardroom",
    "Whimsical Cloud Cityscape",
    "Spellbinding Constellation Network",
    "Celestial Corporate Garden",
    "Astral Projection Workspace",
    "Elixir of Innovation Studio",
    "Charmed Quantum Computer",
    "Sorcerer's Data Center",
    "Majestic Unicorn Start-up",
    "Fairy-tale Virtual Reality",
    "Mythical Phoenix Incubator",
    "Arcane Holographic Interface",
    "Supernatural Machine Learning",
    "Mystic Algorithmic Cauldron",
    "Enchanted Tech Tree"
]

essentials = [
    "Responsive Web Design",
    "User Interface Elements",
    "Coding and Programming Languages",
    "Search Engine Optimization",
    "Web Security and Privacy",
    "Website Analytics Dashboard",
    "Mobile App Development",
    "Social Media Integration",
    "E-commerce Shopping Cart",
    "Content Management System",
    "Website Hosting and Domain",
    "Web Development Team",
    "Multimedia Integration",
    "User Experience Design",
    "Accessibility and Inclusivity",
    "Email Marketing Campaign",
    "Website Wireframe",
    "Online Collaboration Tools",
    "Customer Support Services",
    "Website Page Speed Optimization",
    "Browser Compatibility Testing",
    "Website Update and Maintenance",
    "Online Advertising and Promotion",
    "Landing Page Optimization",
    "Conversion Rate Optimization",
    "Website Typography and Fonts",
    "Web Development Project Planning",
    "Web Design Color Theory",
    "Web Development Best Practices",
    "Online Portfolio and Resume"
]


professionalImages = [
    "Sleek Modern Office Space",
    "Elegant Business Meeting",
    "Cutting-Edge Technology Showcase",
    "Dynamic Team Collaboration",
    "Innovative Product Presentation",
    "Efficient Workspace Organization",
    "Powerful Corporate Branding",
    "Diverse Professional Networking",
    "Strategic Planning Session",
    "Influential Leadership Conference",
    "Expert Technical Support",
    "Global Supply Chain Management",
    "High-Performance Data Center",
    "Sophisticated Financial Analysis",
    "State-of-the-Art Medical Facility",
    "Inspiring Architectural Design",
    "Advanced Manufacturing Process",
    "Clean Renewable Energy Solutions",
    "Futuristic Urban Transportation",
    "Progressive Sustainable Development"
]


constructionImages = [
    "Panoramic Cityscape Construction",
    "Modern Skyscraper Framework",
    "Innovative Green Building Design",
    "Dynamic Bridge Engineering",
    "Majestic Tower Crane in Action",
    "Sunset Over Construction Site",
    "Busy Urban Infrastructure Development",
    "Aerial View of Expansive Project",
    "Eco-friendly Residential Complex",
    "Futuristic Commercial Architecture",
    "Historic Renovation and Preservation",
    "Industrial Construction Equipment",
    "Efficient Modular Construction",
    "Stunning Interior Fit-Out Progress",
    "Safe and Organized Worksite",
    "Powerful Earthmoving Machinery",
    "Concrete Jungle Transformation",
    "Harmonious Public Space Development",
    "Skyline Changing High-rise",
    "Detailed Blueprint and Model"
]



personal = [
"Healthy breakfast spread",
"Creative workspace inspiration",
"Cozy reading nook",
"Relaxing bubble bath scene",
"Artistic coffee shop vibe",
"Colorful farmers market haul",
"Outdoor hiking adventure",
"Sunny beach day essentials",
"Garden party setup",
"Fashionable outfit of the day",
"Minimalist home decor ideas",
"DIY crafting supplies",
"Romantic candlelit dinner setting",
"Stylish workout attire",
"Vintage record player setup",
"Modern city skyline at sunset",
"Adorable pet in a cute outfit",
"Rustic cabin getaway",
"Dreamy starry night sky",
"Festive holiday decor"
]

athleticPrompts = [
  "Workout essentials for a beginner",
  "How to build strength with resistance bands",
  "Top 10 yoga poses for runners",
  "Why rest days are important for your fitness routine",
  "Healthy snack ideas for pre- and post-workout fuel",
  "Benefits of incorporating HIIT into your workouts",
  "How to properly stretch before and after exercise",
  "Top 5 running trails in your city",
  "Benefits of foam rolling for muscle recovery",
  "How to stay motivated to exercise during the winter months"
]

psych = [
  "Galactic Nebula Explosion",
  "Rainbow Geometric Mandala",
  "Trippy Forest of Neon Trees",
  "Psychedelic Ocean Waves",
  "Cosmic Flower of Life",
  "Intergalactic Kaleidoscope",
  "Crystal Cave Light Show",
  "Luminous Neon Jungle",
  "Electric Plasma Storm",
  "Psychedelic Skyline Cityscape",
  "Intricate Fractal Artwork",
  "Fluorescent Dream World",
  "Ethereal Alien Landscape",
  "Hypnotic Techno Spiral",
  "Enchanted Fairy Garden"
]

tattoo = [

  "Generate a simple tattoo sketch with the themes of magic and mushrooms",
  "Generate a simple tattoo to incorporate waves",
  "Generate a simple tattoo of a wizard shooting his wand at a green light "

]



products= [


  constructionImages,
  professionalImages,
  essentials,
  magical_products,
  personal,
  athleticPrompts,
  tattoo

]

image_xpaths = [
    '//*[@id="mmComponent_images_1"]/ul[1]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[1]/li[2]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[2]/li[1]/div/div/a/div/img',
    '//*[@id="mmComponent_images_1"]/ul[2]/li[2]/div/div/a/div/img'
]

def main():
    service = Service(executable_path=CHROME_DRIVER_PATH)
    driver = webdriver.Chrome(service=service)

    for product_set in products:  # Change from product to product_set
        for product in product_set:  # Iterate over each product in the product_set
            driver.get(BASE_URL)

            try:
                login_button = WebDriverWait(driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, '/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[4]/div/div/div/div[4]/div/div/div/div[2]/a'))
                )
                login_button.click()
                print("Logging in with Face...")
                time.sleep(5)
            except Exception as e:
                print("No login required, continuing...")

            search_box = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="sb_form_q"]'))
            )
            search_box.clear()
            search_box.send_keys(f"Can you make stunning webcontent featuring the following: {product}")
            search_box.submit()

            product_folder_name = product_set[0].split(" ")[0]  # Use the first word of the first product in the product_set as folder name
            product_folder = os.path.join(SAVE_PATH, product_folder_name)  # Create folder path using folder name
            os.makedirs(product_folder, exist_ok=True)  # Create folder if it doesn't exist

            for index, xpath in enumerate(image_xpaths, start=1):
                print(f"Waiting for image {index} to be generated for {product}...")
                try:
                    generated_image = WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.XPATH, xpath))
                    )
                    generated_image_url = generated_image.get_attribute("src")

                    response = request.urlopen(generated_image_url)
                    if response.status == 200:
                        print(f"Saving image")
                        print(f"Saving image {index} for {product}...")
                        with open(os.path.join(product_folder, f"{product.replace(' ', '_')}_img{index}.jpg"), "wb") as file:
                            file.write(response.read())
                        print(f"Image {index} for {product} saved successfully.")
                    else:
                        print(f"Failed to download image {index} for {product} (status code {response.status}).")
                except Exception as e:
                    print(f"Error while downloading image {index} for {product}: {e}")
    driver.quit()

if __name__ == "__main__":
    main()

