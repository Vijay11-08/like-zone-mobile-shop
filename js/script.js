/* ============================================================
   LIKE ZONE MOBILE SHOP — script.js
   Chatbot, WhatsApp, Animations, Navbar
   ============================================================ */

'use strict';

/* ── WhatsApp Helper ─────────────────────────────────────────── */
function openWhatsApp(message) {
  const phone = '919904640764';
  const url = `https://wa.me/${phone}?text=${encodeURIComponent(message)}`;
  window.open(url, '_blank', 'noopener,noreferrer');
}

/* ── Navbar Active Link on Scroll ────────────────────────────── */
(function initNavbar() {
  const navbar   = document.getElementById('mainNavbar');
  const navLinks = document.querySelectorAll('.navbar-nav .nav-link');
  const sections = document.querySelectorAll('section[id], div[id]');

    // Scroll shadow
    window.addEventListener('scroll', () => {
      if (window.scrollY > 50) {
        navbar.style.boxShadow = '0 4px 30px rgba(0,0,0,0.5)';
      } else {
        navbar.style.boxShadow = 'none';
      }
    });

  // Smooth scroll for nav links
  navLinks.forEach(link => {
    link.addEventListener('click', (e) => {
      const href = link.getAttribute('href');
      if (href && href.startsWith('#')) {
        e.preventDefault();
        const target = document.querySelector(href);
        if (target) {
          target.scrollIntoView({ behavior: 'smooth' });
          // Close mobile menu
          const collapse = document.getElementById('navbarContent');
          if (collapse && collapse.classList.contains('show')) {
            const toggler = document.querySelector('.navbar-toggler');
            if (toggler) toggler.click();
          }
        }
      }
    });
  });
})();



/* ── Hero Content Fade-in on Load ────────────────────────────── */
(function initHeroAnimation() {
  const heroContent = document.querySelector('.hero-content');
  const heroVisual  = document.querySelector('.hero-visual');

  if (heroContent) {
    heroContent.style.opacity = '0';
    heroContent.style.transform = 'translateY(30px)';
    setTimeout(() => {
      heroContent.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
      heroContent.style.opacity = '1';
      heroContent.style.transform = 'translateY(0)';
    }, 200);
  }

  if (heroVisual) {
    heroVisual.style.opacity = '0';
    heroVisual.style.transform = 'translateY(30px)';
    setTimeout(() => {
      heroVisual.style.transition = 'opacity 0.8s ease, transform 0.8s ease';
      heroVisual.style.opacity = '1';
      heroVisual.style.transform = 'translateY(0)';
    }, 500);
  }
})();

/* ── Chatbot ─────────────────────────────────────────────────── */
(function initChatbot() {
  const toggle   = document.getElementById('chatbotToggle');
  const window_  = document.getElementById('chatbotWindow');
  const closeBtn = document.getElementById('chatbotClose');
  const minBtn   = document.getElementById('chatbotMinimize');
  const messages = document.getElementById('chatbotMessages');
  const input    = document.getElementById('chatbotInput');
  const icon     = document.getElementById('chatToggleIcon');

  if (!toggle || !window_) return;

  let isOpen      = false;
  let isMinimized = false;
  let chatHistory = [];

  // Bot responses
  const responses = {
    mobiles: {
      text: 'Sure! We deal in smartphones from popular brands including Samsung, Apple, Redmi, Realme, Vivo and Oppo. For current models, prices and availability, please contact us on WhatsApp.',
      actions: [
        { label: '📱 Ask on WhatsApp', type: 'whatsapp', msg: 'Hello, I want to know about mobile phone availability and prices.' }
      ]
    },
    accessories: {
      text: 'We provide a wide range of mobile accessories including mobile covers, tempered glass, chargers, USB cables, earphones and Bluetooth devices.',
      actions: [
        { label: '🎧 Enquire on WhatsApp', type: 'whatsapp', msg: 'Hello, I want to enquire about mobile accessories.' }
      ]
    },
    services: {
      text: 'We provide mobile-related services including accessories, scratch guard installation and repair-related assistance. Feel free to visit us or contact us.',
      actions: [
        { label: '🛠️ Ask on WhatsApp', type: 'whatsapp', msg: 'Hello, I want to enquire about mobile services.' }
      ]
    },
    location: {
      text: 'We are located at Kasturba Dham, Tramba, Rajkot, Gujarat – 360020. You can get directions using the button below.',
      actions: [
        { label: '📍 Get Directions', type: 'directions' }
      ]
    },
    contact: {
      text: 'You can call Like Zone Mobile Shop at +91 99046 40764 or chat with us on WhatsApp anytime.',
      actions: [
        { label: '📞 Call Now', type: 'call' },
        { label: '💬 WhatsApp', type: 'whatsapp', msg: 'Hello Like Zone Mobile Shop, I would like to know more about your products and services.' }
      ]
    }
  };

  // Keyword map for text input
  const keywordMap = [
    { keywords: ['mobile', 'phone', 'smartphone', 'samsung', 'iphone', 'redmi', 'realme', 'vivo', 'oppo', 'xiaomi'], key: 'mobiles' },
    { keywords: ['accessory', 'accessories', 'cover', 'charger', 'cable', 'earphone', 'bluetooth', 'glass', 'tempered'], key: 'accessories' },
    { keywords: ['service', 'repair', 'fix', 'scratch', 'guard', 'screen'], key: 'services' },
    { keywords: ['location', 'address', 'where', 'tramba', 'rajkot', 'kasturba', 'direction', 'map'], key: 'location' },
    { keywords: ['contact', 'call', 'number', 'phone number', 'whatsapp', 'reach'], key: 'contact' }
  ];

  function getTime() {
    return new Date().toLocaleTimeString('en-IN', { hour: '2-digit', minute: '2-digit' });
  }

  function addMessage(text, sender, actions) {
    const msg = document.createElement('div');
    msg.className = `chat-msg ${sender}`;

    const bubble = document.createElement('div');
    bubble.className = 'msg-bubble';
    bubble.textContent = text;

    const time = document.createElement('div');
    time.className = 'msg-time';
    time.textContent = getTime();

    msg.appendChild(bubble);
    msg.appendChild(time);

    if (actions && actions.length > 0) {
      const actionsDiv = document.createElement('div');
      actionsDiv.className = 'msg-actions';

      actions.forEach(action => {
        const btn = document.createElement('button');
        btn.className = 'msg-action-btn';
        btn.textContent = action.label;

        if (action.type === 'whatsapp') {
          btn.classList.add('wa-action');
          btn.addEventListener('click', () => openWhatsApp(action.msg));
        } else if (action.type === 'call') {
          btn.addEventListener('click', () => { window.location.href = 'tel:+919904640764'; });
        } else if (action.type === 'directions') {
          btn.addEventListener('click', () => {
            window.open('https://www.google.com/maps/search/Like+Zone+Mobile+Shop+Kasturba+Dham+Tramba+Rajkot', '_blank', 'noopener,noreferrer');
          });
        }

        actionsDiv.appendChild(btn);
      });

      msg.appendChild(actionsDiv);
    }

    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
    chatHistory.push({ text, sender });
  }

  function showTyping() {
    const typing = document.createElement('div');
    typing.className = 'chat-msg bot';
    typing.id = 'typingIndicator';

    const indicator = document.createElement('div');
    indicator.className = 'typing-indicator';
    indicator.innerHTML = '<div class="typing-dot"></div><div class="typing-dot"></div><div class="typing-dot"></div>';

    typing.appendChild(indicator);
    messages.appendChild(typing);
    messages.scrollTop = messages.scrollHeight;
  }

  function removeTyping() {
    const typing = document.getElementById('typingIndicator');
    if (typing) typing.remove();
  }

  function botReply(key) {
    showTyping();
    setTimeout(() => {
      removeTyping();
      const resp = responses[key];
      if (resp) {
        addMessage(resp.text, 'bot', resp.actions);
      } else {
        addMessage("I'm not sure about that. Please contact us on WhatsApp or call us at +91 99046 40764 for assistance.", 'bot', [
          { label: '💬 WhatsApp Us', type: 'whatsapp', msg: 'Hello Like Zone Mobile Shop, I need assistance.' }
        ]);
      }
    }, 900);
  }

  function detectIntent(text) {
    const lower = text.toLowerCase();
    for (const entry of keywordMap) {
      if (entry.keywords.some(kw => lower.includes(kw))) {
        return entry.key;
      }
    }
    return null;
  }

  // Open/close
  function openChat() {
    isOpen = true;
    isMinimized = false;
    window_.classList.add('open');
    window_.setAttribute('aria-hidden', 'false');
    toggle.setAttribute('aria-expanded', 'true');
    icon.className = 'bi bi-x-lg';

    // Welcome message on first open
    if (chatHistory.length === 0) {
      setTimeout(() => {
        addMessage('👋 Hello! Welcome to Like Zone Mobile Shop. How can I help you today?', 'bot');
        setTimeout(() => {
          addMessage('You can ask me about our mobile phones, accessories, services, location or contact details.', 'bot');
        }, 600);
      }, 300);
    }

    if (input) input.focus();
  }

  function closeChat() {
    isOpen = false;
    window_.classList.remove('open');
    window_.setAttribute('aria-hidden', 'true');
    toggle.setAttribute('aria-expanded', 'false');
    icon.className = 'bi bi-chat-dots-fill';
  }

  toggle.addEventListener('click', () => {
    if (isOpen) closeChat(); else openChat();
  });

  if (closeBtn) closeBtn.addEventListener('click', closeChat);

  if (minBtn) {
    minBtn.addEventListener('click', () => {
      isMinimized = !isMinimized;
      const body = window_.querySelector('.chatbot-messages');
      const qr   = window_.querySelector('.chatbot-quick-replies');
      const inp  = window_.querySelector('.chatbot-input-area');
      if (isMinimized) {
        if (body) body.style.display = 'none';
        if (qr)   qr.style.display   = 'none';
        if (inp)  inp.style.display  = 'none';
        minBtn.innerHTML = '<i class="bi bi-chevron-up"></i>';
      } else {
        if (body) body.style.display = '';
        if (qr)   qr.style.display   = '';
        if (inp)  inp.style.display  = '';
        minBtn.innerHTML = '<i class="bi bi-dash-lg"></i>';
      }
    });
  }

  // Keyboard close
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && isOpen) closeChat();
  });

  // Quick reply buttons
  window.sendQuickReply = function(key) {
    const labels = {
      mobiles:     '📱 Mobile Phones',
      accessories: '🎧 Accessories',
      services:    '🛠️ Services',
      location:    '📍 Location',
      contact:     '📞 Contact'
    };
    addMessage(labels[key] || key, 'user');
    botReply(key);
  };

  // Text input
  window.handleChatInput = function(e) {
    if (e.key === 'Enter') handleSendMessage();
  };

  window.handleSendMessage = function() {
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;

    addMessage(text, 'user');
    input.value = '';

    const intent = detectIntent(text);
    botReply(intent || 'unknown');
  };
})();

/* ── Floating Buttons Visibility ─────────────────────────────── */
(function initFloatingButtons() {
  const floatingBtns = document.querySelector('.floating-buttons');
  if (!floatingBtns) return;

  // Show after scrolling past hero
  window.addEventListener('scroll', () => {
    if (window.scrollY > 300) {
      floatingBtns.style.opacity = '1';
      floatingBtns.style.transform = 'translateY(0)';
    } else {
      floatingBtns.style.opacity = '0';
      floatingBtns.style.transform = 'translateY(20px)';
    }
  });

  // Initial state
  floatingBtns.style.opacity = '0';
  floatingBtns.style.transform = 'translateY(20px)';
  floatingBtns.style.transition = 'opacity 0.4s ease, transform 0.4s ease';
})();



/* ── Smooth Anchor Scrolling (fallback for non-nav links) ────── */
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
  anchor.addEventListener('click', function(e) {
    const href = this.getAttribute('href');
    if (href === '#') return;
    const target = document.querySelector(href);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth' });
    }
  });
});