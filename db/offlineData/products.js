const offlineProducts = [
  {
    id: 1,
    name: 'Reishi Mushroom Tincture',
    description:
      'Boost your immune system with our organic Reishi Mushroom Tincture. Made from high-quality Reishi mushrooms, this tincture supports overall wellness and vitality.',
    img_url: '/products/reishi-tincture.jpg',
    price: 29.99,
    rating: 4.5,
    tags: ['mushroom', 'tinctures', 'immunity']
  },
  {
    id: 2,
    name: 'Delta 8 Tincture',
    description:
      'Experience relaxation and stress relief with our Delta 8 Tincture. Made from premium hemp extracts, this tincture promotes a calm and balanced state of mind.',
    img_url: '/products/delta-8-tincture.jpg',
    price: 39.99,
    rating: 4.7,
    tags: ['delta-8', 'tinctures', 'stress']
  },
  {
    id: 3,
    name: 'Delta 8 Vape Cartridge',
    description:
      'Enjoy the benefits of Delta 8 with our convenient vape cartridge. Designed for easy use, this cartridge delivers a smooth and flavorful experience.',
    img_url: '/products/delta-8-vape.jpg',
    price: 34.99,
    rating: 4.2,
    tags: ['delta-8', 'cartridge', 'vape']
  },
  {
    id: 4,
    name: 'Delta 8 Gummies',
    description:
      'Satisfy your sweet tooth and relax with our delicious Delta 8 Gummies. These tasty edibles provide a consistent and enjoyable experience, perfect for on-the-go use.',
    img_url: '/products/delta-8-gummies.jpg',
    price: 24.99,
    rating: 4.8,
    tags: ['delta-8', 'gummies', 'stress']
  },
  {
    id: 5,
    name: 'Natural Ashwagandha Supplement',
    description:
      'Enhance your stress management and support your adrenal health with our Natural Ashwagandha Supplement. This powerful adaptogen helps your body adapt to stress and promotes overall well-being.',
    img_url: '/products/ashwagandha-supplement.jpg',
    price: 19.99,
    rating: 4.6,
    tags: ['supplements', 'anxiety', 'stress']
  },
  {
    id: 6,
    name: 'Amethyst Crystal',
    description:
      'Promote spiritual growth and balance your energies with our beautiful Amethyst Crystal. This powerful stone is perfect for meditation and enhancing your intuition.',
    img_url: '/products/amethyst-crystal.jpg',
    price: 15.99,
    rating: 4.9,
    tags: ['spiritual', 'crystals', 'meditation']
  },
  {
    id: 7,
    name: 'Rose Quartz Crystal',
    description:
      'Open your heart and attract love with our soothing Rose Quartz Crystal. Known as the stone of unconditional love, this beautiful crystal promotes self-love, forgiveness, and emotional healing.',
    img_url: '/products/rose-quartz-crystal.jpg',
    price: 12.99,
    rating: 5.0,
    tags: ['crystals', 'love', 'healing']
  },
  {
    id: 8,
    name: 'Clear Quartz Crystal',
    description:
      'Amplify your intentions and manifest your desires with our versatile Clear Quartz Crystal. This powerful stone cleanses and charges your energy, making it perfect for any spiritual practice.',
    img_url: '/products/clear-quartz-crystal.jpg',
    price: 10.99,
    rating: 4.4,
    tags: ['crystals', 'manifestation', 'intention']
  },
  {
    id: 9,
    name: 'Turmeric Curcumin Supplement',
    description:
      'Support your joint health and reduce inflammation with our Turmeric Curcumin Supplement. Packed with powerful antioxidants, this natural supplement promotes overall wellness and optimal health.',
    img_url: '/products/turmeric-curcumin-supplement.jpg',
    price: 22.99,
    rating: 4.7,
    tags: ['supplements', 'inflammation', 'joint']
  },
  {
    id: 10,
    name: 'Lions Mane Mushroom Tincture',
    description:
      'Enhance your cognitive function and support your nervous system with our Lions Mane Mushroom Tincture. This powerful nootropic promotes mental clarity, focus, and overall brain health.',
    img_url: '/products/lions-mane-tincture.jpg',
    price: 32.99,
    rating: 4.8,
    tags: ['mushroom', 'tinctures', 'brain']
  },
  {
    id: 11,
    name: 'Cordyceps Mushroom Capsules',
    description:
      'Boost your energy and athletic performance with our Cordyceps Mushroom Capsules. These capsules are made from high-quality Cordyceps mushrooms, known for their natural energy-enhancing properties.',
    img_url: '/products/cordyceps-capsules.jpg',
    price: 28.99,
    rating: 4.6,
    tags: ['mushroom', 'capsules', 'energy']
  },
  {
    id: 12,
    name: 'CBD Chocolate Bar',
    description:
      'Indulge in our delicious CBD Chocolate Bar, infused with premium CBD for relaxation and stress relief. This delightful treat provides a calming experience while satisfying your chocolate cravings.',
    img_url: '/products/cbd-chocolate.jpg',
    price: 14.99,
    rating: 4.9,
    tags: ['cbd', 'chocolate', 'stress']
  },
  {
    id: 13,
    name: 'Sleep Support Supplement',
    description:
      'Improve your sleep quality and wake up refreshed with our Sleep Support Supplement. Formulated with natural ingredients, this supplement helps you fall asleep faster and stay asleep longer.',
    img_url: '/products/sleep-support-supplement.jpg',
    price: 19.99,
    rating: 4.7,
    tags: ['supplements', 'sleep', 'stress']
  },
  {
    id: 14,
    name: 'Delta-9 Chocolate Bar',
    description:
      'Enjoy the uplifting effects of our Delta-9 Chocolate Bar. Infused with premium Delta-9, this decadent chocolate treat provides a balanced and enjoyable experience.',
    img_url: '/products/delta-9-chocolate.jpg',
    price: 24.99,
    rating: 4.8,
    tags: ['delta-9', 'chocolate', 'stress']
  },
  {
    id: 15,
    name: 'Nootropic Energy Supplement',
    description:
      'Enhance your mental focus and boost your energy levels with our Nootropic Energy Supplement. This powerful formula contains natural ingredients to help you stay alert and focused throughout the day.',
    img_url: '/products/nootropic-energy-supplement.jpg',
    price: 21.99,
    rating: 4.5,
    tags: ['supplements', 'energy', 'focus']
  },
  {
    id: 16,
    name: 'Immunity Booster Supplement',
    description:
      'Support your immune system and overall health with our Immunity Booster Supplement. Packed with essential vitamins and minerals, this formula promotes a strong immune response and optimal wellness.',
    img_url: '/products/immunity-booster-supplement.jpg',
    price: 23.99,
    rating: 4.6,
    tags: ['supplements', 'immune', 'health']
  },
  {
    id: 17,
    name: 'Aphrodisiac Herbal Blend',
    description:
      'Enhance your love life and ignite passion with our Aphrodisiac Herbal Blend. This carefully crafted blend of natural herbs supports healthy libido and increased vitality.',
    img_url: '/products/aphrodisiac-herbal-blend.jpg',
    price: 18.99,
    rating: 4.4,
    tags: ['herbal', 'love', 'libido']
  },
  {
    id: 18,
    name: 'Mood Support Supplement',
    description:
      'Elevate your mood and enhance emotional balance with our Mood Support Supplement. This natural formula helps regulate mood swings, reduce stress, and promote a positive outlook on life.',
    img_url: '/products/mood-support-supplement.jpg',
    price: 25.99,
    rating: 4.7,
    tags: ['supplements', 'mood', 'stress']
  },
  {
    id: 19,
    name: 'Anxiety Relief Supplement',
    description:
      'Ease anxiety and promote relaxation with our Anxiety Relief Supplement. This natural formula contains a blend of herbs and nutrients to help you stay calm and focused in stressful situations.',
    img_url: '/products/anxiety-relief-supplement.jpg',
    price: 20.99,
    rating: 4.8,
    tags: ['supplements', 'anxiety', 'stress']
  },
  {
    id: 20,
    name: 'CBD Gummies',
    description:
      'Enjoy a tasty and convenient way to experience the benefits of CBD with our CBD Gummies. Made with premium CBD extracts, these gummies provide a calming and enjoyable experience.',
    img_url: '/products/cbd-gummies.jpg',
    price: 29.99,
    rating: 4.9,
    tags: ['cbd', 'gummies', 'stress']
  }, {
    id: 21,
    name: 'Chakra Balancing Tea Blend',
    description:
      'Experience a harmonious balance of energy with our Chakra Balancing Tea Blend. This unique herbal blend combines carefully selected herbs that help to align and balance your chakras, promoting a sense of inner peace and spiritual well-being.',
    img_url: '/products/chakra-balancing-tea.jpg',
    price: 18.99,
    rating: 4.9,
    tags: ['tea', 'chakra', 'balance']
  },
  {
    id: 22,
    name: 'Sacred Palo Santo Smudge Sticks',
    description:
      'Cleanse your space and uplift your spirit with our Sacred Palo Santo Smudge Sticks. These sustainably harvested sticks are perfect for purifying your environment and inviting positive energy into your life.',
    img_url: '/products/palo-santo-smudge-sticks.jpg',
    price: 14.99,
    rating: 4.8,
    tags: ['smudge', 'palo santo', 'energy']
  },
  {
    id: 23,
    name: 'Organic Kava Kava Root Powder',
    description:
      'Relieve stress and promote relaxation with our Organic Kava Kava Root Powder. This potent natural remedy has been used for centuries in traditional ceremonies to encourage a deep sense of calm and spiritual connection.',
    img_url: '/products/kava-kava-root-powder.jpg',
    price: 24.99,
    rating: 4.7,
    tags: ['kava', 'kava kava', 'stress']
  },
  {
    id: 24,
    name: 'Third Eye Awakening Herbal Tincture',
    description:
      'Enhance your intuition and spiritual insight with our Third Eye Awakening Herbal Tincture. This powerful blend of herbs supports the opening of your third eye, helping you to deepen your connection to your inner wisdom.',
    img_url: '/products/third-eye-awakening-tincture.jpg',
    price: 28.99,
    rating: 4.6,
    tags: ['herbal', 'tincture', 'third eye']
  },
  {
    id: 25,
    name: 'Astral Projection Incense Blend',
    description:
      'Prepare for a mystical journey with our Astral Projection Incense Blend. This enchanting blend of herbs and resins is specifically designed to support deep meditation and astral travel, allowing you to explore the spiritual realm with ease.',
    img_url: '/products/astral-projection-incense.jpg',
    price: 19.99,
    rating: 4.5,
    tags: ['incense', 'astral', 'projection']
  },
  {
    id: 26,
    name: 'Organic beard oil',
    description:
      'Prepare for a mystical journey with our Astral Projection Incense Blend. This enchanting blend of herbs and resins is specifically designed to support deep meditation and astral travel, allowing you to explore the spiritual realm with ease.',
    img_url: '/products/astral-projection-incense.jpg',
    price: 10.99,
    rating: 4.5,
    tags: ['beard', 'oil', 'beard oil']
  },
];

export default offlineProducts;
