/* OnTalent — progressive enhancement. Everything degrades gracefully without JS. */
(function () {
  "use strict";

  /* ---- EmailJS contact form ---- */
  var contactForm = document.getElementById("contact-form");
  if (contactForm) {
    var script = document.createElement("script");
    script.src = "https://cdn.jsdelivr.net/npm/@emailjs/browser@3/dist/email.min.js";
    script.onload = function () { emailjs.init("MSNPLtMZlMWp2V-ER"); };
    document.head.appendChild(script);

    var emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

    function setFieldError(id, msg) {
      var el = document.getElementById(id);
      var hint = document.getElementById(id + "-err");
      el.setAttribute("aria-invalid", "true");
      el.classList.add("form-input--invalid");
      if (hint) { hint.textContent = msg; hint.style.display = "block"; }
    }

    function clearFieldError(id) {
      var el = document.getElementById(id);
      var hint = document.getElementById(id + "-err");
      el.removeAttribute("aria-invalid");
      el.classList.remove("form-input--invalid");
      if (hint) { hint.style.display = "none"; }
    }

    /* Live validation on blur */
    document.getElementById("cf-name").addEventListener("blur", function () {
      this.value.trim() ? clearFieldError("cf-name") : setFieldError("cf-name", "Please enter your name.");
    });
    document.getElementById("cf-email").addEventListener("blur", function () {
      emailRe.test(this.value.trim()) ? clearFieldError("cf-email") : setFieldError("cf-email", "Please enter a valid email address.");
    });
    document.getElementById("cf-message").addEventListener("blur", function () {
      this.value.trim() ? clearFieldError("cf-message") : setFieldError("cf-message", "Please enter a message.");
    });

    contactForm.addEventListener("submit", function (e) {
      e.preventDefault();
      var nameVal    = document.getElementById("cf-name").value.trim();
      var emailVal   = document.getElementById("cf-email").value.trim();
      var messageVal = document.getElementById("cf-message").value.trim();

      var valid = true;
      if (!nameVal)                { setFieldError("cf-name",    "Please enter your name.");            valid = false; }
      else                         { clearFieldError("cf-name"); }
      if (!emailRe.test(emailVal)) { setFieldError("cf-email",   "Please enter a valid email address."); valid = false; }
      else                         { clearFieldError("cf-email"); }
      if (!messageVal)             { setFieldError("cf-message", "Please enter a message.");            valid = false; }
      else                         { clearFieldError("cf-message"); }
      if (!valid) return;

      var btn = contactForm.querySelector("button[type=submit]");
      var ok = document.getElementById("form-ok");
      var err = document.getElementById("form-err");
      if (ok) ok.className = "form-status";
      if (err) err.className = "form-status";
      btn.disabled = true;
      btn.textContent = "Sending…";
      emailjs.send("service_vsqf7kr", "template_a4qnd8f", {
        name: nameVal, email: emailVal, message: messageVal
      }).then(function () {
        if (ok) ok.className = "form-status form-status--ok";
        contactForm.reset();
        ["cf-name","cf-email","cf-message"].forEach(clearFieldError);
        btn.disabled = false;
        btn.textContent = "Send message";
      }, function () {
        if (err) err.className = "form-status form-status--err";
        btn.disabled = false;
        btn.textContent = "Send message";
      });
    });
  }

  /* ---- Mobile nav toggle ---- */
  var toggle = document.querySelector(".nav-toggle");
  var nav = document.getElementById("site-nav");
  if (toggle && nav) {
    toggle.addEventListener("click", function () {
      var open = nav.classList.toggle("is-open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    // Close the menu when a link is tapped
    nav.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        nav.classList.remove("is-open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---- Footer year ---- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });

  /* ---- Respect reduced motion ---- */
  var reduce = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)").matches;
  var reduceMotionQuery = window.matchMedia && window.matchMedia("(prefers-reduced-motion: reduce)");

  /* ---- Home hero page-motion animation ---- */
  function drawStar(context, x, y, radius, color) {
    var inner = radius * 0.44;
    context.beginPath();
    for (var i = 0; i < 10; i += 1) {
      var angle = -Math.PI / 2 + (i * Math.PI) / 5;
      var length = i % 2 === 0 ? radius : inner;
      var px = x + Math.cos(angle) * length;
      var py = y + Math.sin(angle) * length;
      if (i === 0) context.moveTo(px, py);
      else context.lineTo(px, py);
    }
    context.closePath();
    context.fillStyle = color;
    context.fill();
  }

  function createHeroNetwork(canvas) {
    var context = canvas.getContext("2d");
    if (!context) return null;

    var palette = ["#FF6A4D", "#F25C54", "#199FB0", "#2F9E68", "#E0A12E", "#7A5CD0", "#F2EEF8"];
    var frame;
    var particles = [];

    function resize() {
      var ratio = window.devicePixelRatio || 1;
      var rect = canvas.getBoundingClientRect();
      canvas.width = Math.floor(rect.width * ratio);
      canvas.height = Math.floor(rect.height * ratio);
      context.setTransform(ratio, 0, 0, ratio, 0, 0);

      var count = Math.min(58, Math.max(28, Math.floor(rect.width / 25)));
      particles = Array.from({ length: count }, function (_, index) {
        return {
          x: Math.random() * rect.width,
          y: Math.random() * rect.height,
          vx: (Math.random() - .5) * .16,
          vy: (Math.random() - .5) * .16,
          radius: Math.random() * 2.4 + 1.8,
          color: palette[index % palette.length],
          shape: index % 11 === 0 ? "star" : "dot"
        };
      });
    }

    function draw() {
      var width = canvas.clientWidth;
      var height = canvas.clientHeight;
      var isReduced = reduceMotionQuery && reduceMotionQuery.matches;

      context.clearRect(0, 0, width, height);

      if (!isReduced) {
        particles.forEach(function (point) {
          point.x += point.vx;
          point.y += point.vy;
          if (point.x < 0 || point.x > width) point.vx *= -1;
          if (point.y < 0 || point.y > height) point.vy *= -1;
        });
      }

      for (var i = 0; i < particles.length; i += 1) {
        for (var j = i + 1; j < particles.length; j += 1) {
          var a = particles[i];
          var b = particles[j];
          var dx = a.x - b.x;
          var dy = a.y - b.y;
          var distance = Math.sqrt(dx * dx + dy * dy);
          if (distance < 170) {
            context.beginPath();
            context.moveTo(a.x, a.y);
            context.lineTo(b.x, b.y);
            context.strokeStyle = "rgba(242, 238, 248, " + (0.2 * (1 - distance / 170)) + ")";
            context.lineWidth = 1.15;
            context.stroke();
          }
        }
      }

      particles.forEach(function (point, index) {
        context.globalAlpha = index % 5 === 0 ? .72 : .56;
        if (point.shape === "star") drawStar(context, point.x, point.y, point.radius * 3.8, point.color);
        else {
          context.beginPath();
          context.arc(point.x, point.y, point.radius, 0, Math.PI * 2);
          context.fillStyle = point.color;
          context.fill();
        }
        context.globalAlpha = 1;
      });

      if (!isReduced) frame = requestAnimationFrame(draw);
    }

    function restart() {
      cancelAnimationFrame(frame);
      resize();
      draw();
    }

    restart();
    return restart;
  }

  var heroNetwork = document.querySelector(".hero__network");
  var restartHeroNetwork = heroNetwork ? createHeroNetwork(heroNetwork) : null;
  if (restartHeroNetwork) {
    window.addEventListener("resize", restartHeroNetwork);
  }

  /* ---- Scroll reveal ---- */
  var reveals = document.querySelectorAll("[data-reveal]");
  if (reduce || !("IntersectionObserver" in window)) {
    reveals.forEach(function (el) { el.classList.add("is-visible"); });
  } else {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add("is-visible");
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.12, rootMargin: "0px 0px -40px 0px" });
    reveals.forEach(function (el) { io.observe(el); });
  }

  /* ---- Stat count-up ---- */
  var counters = document.querySelectorAll("[data-count]");
  function animateCount(el) {
    var target = parseFloat(el.getAttribute("data-count"));
    var suffix = el.getAttribute("data-suffix") || "";
    if (reduce || isNaN(target)) { el.textContent = target + suffix; return; }
    var start = null, dur = 1100;
    function step(ts) {
      if (!start) start = ts;
      var p = Math.min((ts - start) / dur, 1);
      var eased = 1 - Math.pow(1 - p, 3);
      el.textContent = Math.round(target * eased) + suffix;
      if (p < 1) requestAnimationFrame(step);
    }
    requestAnimationFrame(step);
  }
  if ("IntersectionObserver" in window && !reduce) {
    var co = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) { animateCount(entry.target); co.unobserve(entry.target); }
      });
    }, { threshold: 0.5 });
    counters.forEach(function (el) { co.observe(el); });
  }
})();
