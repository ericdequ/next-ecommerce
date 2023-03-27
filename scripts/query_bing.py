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

yogaParallax = [
    "Sunrise Yoga Flow",
    "Tranquil Zen Garden",
    "Harmonious Lotus Pond",
    "Mountain Serenity Retreat",
    "Tropical Beach Meditation",
    "Elegant Bamboo Studio",
    "Peaceful Forest Sanctuary",
    "Candlelit Mindfulness Space",
    "Graceful Yoga Silhouettes",
    "Vibrant Chakra Alignment",
    "Soothing Aerial Yoga",
    "Majestic Waterfall Sanctuary",
    "Starry Night Yoga Session",
    "Sacred Geometry Studio",
    "Mind-Body Balance Bridge",
    "Spiritual Desert Oasis",
    "Blossoming Yoga Garden",
    "Floating Yoga Pavilion",
    "Yoga among the Clouds",
    "Energy Flow Labyrinth"
]


cult = [
"Divine Nature Temple ",
"Cosmic Energy Center ",
"Sacred Fire Ceremony",
"Mystic Moonlit Forest",
"Enchanted Crystal Cave",
"Celestial Sky Meditation",
"Elemental Earth Ritual",
"Angelic Chanting Circle",
"Serene Waterfall Sanctuary",
"Ancient Wisdom Library",
"Awakening Sunrise Celebration",
"Celestial Alignment Ceremony",
"Sacred Sound Healing Circle",
"Elemental Magic Garden",
"Lunar Eclipse Gathering",
"Pristine Mountain Peak Meditation",
"Oceanic Dream Retreat",
"Mystic Pyramid Sanctuary",
"Golden Sunset Yoga Session",
"Shamanic Medicine Wheel Ceremony"
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

  cult,
  yogaParallax,
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
            search_box.send_keys(f"can you make a stunning product image for {product}")
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

