


// Responsive navbar

const toggleBtn = document.querySelector('.toggle_btn');
const toggleBtnIcon = document.querySelector('.toggle_btn i')
const toggleBtn_Icon = document.getElementById('toggle-btn');
const dropdownMenu = document.querySelector('.dropdown_menu');


toggleBtn.onclick = function (){
    dropdownMenu.classList.toggle('open')
    const isOpen = dropdownMenu.classList.contains('open')

    toggleBtnIcon.classList = isOpen ? 'ri-close-line' : 'ri-menu-line';

}





//  Multilanguage support


const langEl = document.querySelector('.langWrap');
const link = document.querySelectorAll('a');
const titleEl = document.querySelector('.l_title');
const subtitleEl = document.querySelector('.l_subtitle');
const descrEl = document.querySelector('.l_description');



link.forEach(el => {
    el.addEventListener('click', () => {
        langEl.querySelector('.active').classList.remove('active');
        el.classList.add('active');

        const attr = el.getAttribute('language');
   
        titleEl.textContent = data[attr].title;
        subtitleEl.textContent = data[attr].subtitle;
        descrEl.textContent = data[attr].description;
    });

});


var data = {
    "english":
    {
        "title": "Delightful Greece",
        "subtitle": "Get to know the  Delightful Greece",
        "description": "Lorem ipsum dolor sit amet consectetur adipisicing elit. Illo, quaerat consequatur, ipsum voluptatibus quasi id eius nulla amet perspiciatis explicabo officia. Quis expedita eligendi dicta repudiandae maxime, voluptas quos temporibus."
    },
    "norwegian":
    {
        "title": "Deilig Hellas",
        "subtitle": "BLi kjent me den deilige Hellas",
        "description": "Her blir du kjent med steder, mennesker, produkter og mange andre sider av den Deilige Hellas"
    },
    "greek":
    {
        "title": "Γοητευτικη Ελλαδα",
        "subtitle": "Γνωρισε απο κοντα την γοητευτικη Ελλαδα.",
        "description": "Ελατε να γνωρισουμε τισ γοητευτικες γωνιες της Ελλαδασ, τους ανθρωπους, τα προιοντα και τα φαγητα και αλλα πολλα της γοητευτικης Ελλαδας."
    }
}



var food_data = {
    "english": {
        "foody_title": "Eirini",
        "foody_description":"Hi. I am Eirini from Paxxi, an award winning blog with new video recipes every week, broadcasting from the island of Crete. My channel is completely independent and driven by my passion for a healthier, home cooking. If I can do it, you can too! Any mentioned brands are only because I personally use them. All sponsors are clearly mentioned in the description of the video."
    },
    "greek":{
        "foody_title":"Ειρήνη",
        "foody_description":"Γεια σας είμαι η Ειρήνη από το Paxxi. Το Paxxi είναι βραβευμένο blog μαγειρικής από την Κρήτη με νέα επεισόδια κάθε εβδομάδα. Το κανάλι μας είναι εντελώς ανεξάρτητο και διατηρείται από την αγάπη μας για τη σπιτική μαγειρική. Αν μπορώ να το κάνω εγώ μπορείς κι εσύ! *ΚΑΝΕ ΔΩΡΕΑΝ ΕΓΓΡΑΦΗ ΣΗΜΕΡΑ*Όποιες αναφορές σε brands είναι καθαρά λόγω προσωπικής προτίμησης. Σε περίπτωση σπόνσορα/προβολής αυτό αναφέρεται με ευδιάκριτο τρόπο στην περιγραφή του βίντεο. Δες αναλυτικά όλες τις συνταγές και άλλα τιπς στο www.paxxi.gr."
    },
    "english": {
        "foody_title": "Akis",
        "foody_description":"Hi Guys and welcome to my channel! Visit my English YouTube channel Akis Petretzikis Kitchen: http://bit.ly/akiskitchenen . A place with a true variety of flavors, aromas and culinary experiences! Here you will find the simplest to the most special recipes! Get ready to cook easy, quick, tasty recipes and if you are looking for subversive but also everyday recipes you are in the right place! Don't forget to leave me a comment on what you want to see! Comment, like & share if you like my recipes"
    },
    "greek":{
        "foody_title":"Άκης Πετρετζίκης",
        "foody_description":"Γεια σας παιδιά και καλώς ήρθατε στο κανάλι μου! Ένα πραγματικό πολυχώρο γεύσεων, αρωμάτων και μαγειρικών εμπειριών! Εδώ θα βρείτε από τις πιο απλές μέχρι και τις πιο ιδιαίτερες συνταγές! Eτοιμαστείτε να μαγειρέψουμε παρέα εύκολες, γρήγορες, νόστιμες συνταγές κι αν ψάχνετε ανατρεπτικές, αλλά και καθημερινές συνταγές είστε στο σωστό μέρος! Μην ξεχάσετε να μου αφήσετε comment για το τι θέλετε να δείτε! Comment, like & share αν σας αρέσουν!"
    },
}