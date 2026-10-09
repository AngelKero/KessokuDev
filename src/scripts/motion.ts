// src/scripts/motion.ts - Kessoku Dev Awwwards-Caliber Motion System
import { gsap } from 'gsap';
import { ScrollTrigger } from 'gsap/ScrollTrigger';
import { SplitText } from 'gsap/SplitText';
import { ScrambleTextPlugin } from 'gsap/ScrambleTextPlugin';
import Lenis from 'lenis';

gsap.registerPlugin(ScrollTrigger, SplitText, ScrambleTextPlugin);

let activeMatchMedia: gsap.MatchMedia | null = null;
let activeLenis: Lenis | null = null;
let activeTickerFn: ((time: number) => void) | null = null;

export function initMotionSystem() {
  // Teardown previous instances if re-initializing
  if (activeMatchMedia) {
    activeMatchMedia.revert();
    activeMatchMedia = null;
  }
  if (activeTickerFn) {
    gsap.ticker.remove(activeTickerFn);
    activeTickerFn = null;
  }
  if (activeLenis) {
    activeLenis.destroy();
    activeLenis = null;
  }
  ScrollTrigger.getAll().forEach((t) => t.kill());

  // 1. Initialize Lenis Smooth Scroll with single GSAP ticker sync
  const lenis = new Lenis({
    duration: 1.2,
    easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
    orientation: 'vertical',
    smoothWheel: true,
  });
  activeLenis = lenis;

  // Expose on window for diagnostics and interoperability
  (window as any).lenis = lenis;
  (window as any).gsap = gsap;
  (window as any).ScrollTrigger = ScrollTrigger;

  lenis.on('scroll', ScrollTrigger.update);
  window.addEventListener('scroll', () => ScrollTrigger.update(), { passive: true });

  const tickerCallback = (time: number) => {
    lenis.raf(time * 1000);
  };
  activeTickerFn = tickerCallback;
  gsap.ticker.add(tickerCallback);
  gsap.ticker.lagSmoothing(0);

  // Smooth anchor scrolling
  document.querySelectorAll<HTMLAnchorElement>('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', (e) => {
      const href = anchor.getAttribute('href');
      if (href && href !== '#' && href.length > 1) {
        const target = document.querySelector(href);
        if (target) {
          e.preventDefault();
          lenis.scrollTo(target as HTMLElement, { offset: -60, duration: 1.1 });
        }
      }
    });
  });

  // Refresh ScrollTrigger when layout & fonts settle
  if (document.fonts?.ready) {
    document.fonts.ready.then(() => ScrollTrigger.refresh());
  }
  window.addEventListener('load', () => ScrollTrigger.refresh());

  // Setup matchMedia for responsive and accessible motion
  const mm = gsap.matchMedia();
  activeMatchMedia = mm;

  mm.add('(prefers-reduced-motion: no-preference)', () => {
    // -------------------------------------------------------------
    // A. HERO FOCAL OVERTURE
    // -------------------------------------------------------------
    const heroTl = gsap.timeline({ defaults: { ease: 'power3.out' } });

    // Scramble Header Technical Stamps
    const scrambleElements = document.querySelectorAll<HTMLElement>('[data-scramble]');
    scrambleElements.forEach((el) => {
      const originalText = el.getAttribute('data-scramble') || el.textContent || '';
      gsap.to(el, {
        duration: 1.2,
        scrambleText: {
          text: originalText,
          chars: '01X_#<>[]',
          speed: 0.35,
          revealDelay: 0.15,
        },
        ease: 'none',
        delay: 0.1,
      });
    });

    // Hero Trust Badge
    const heroBadge = document.querySelector('[data-hero-badge]');
    if (heroBadge) {
      heroTl.fromTo(
        heroBadge,
        { opacity: 0, y: -16, scale: 0.96 },
        { opacity: 1, y: 0, scale: 1, duration: 0.7 },
        0.1
      );
    }

    // Hero Title Reveal with SplitText mask
    const heroTitle = document.getElementById('hero-title');
    if (heroTitle) {
      const split = new SplitText(heroTitle, {
        type: 'lines,words',
        linesClass: 'overflow-hidden py-0.5',
        wordsClass: 'split-word inline-block will-change-transform',
        autoSplit: true,
      });

      heroTl.fromTo(
        split.words,
        { opacity: 0, yPercent: 110 },
        {
          opacity: 1,
          yPercent: 0,
          stagger: 0.025,
          duration: 0.95,
          ease: 'power4.out',
        },
        0.2
      );
    }

    // Hero Paragraph Description
    const heroDesc = document.querySelector('[data-hero-desc]');
    if (heroDesc) {
      heroTl.fromTo(
        heroDesc,
        { opacity: 0, y: 18 },
        { opacity: 1, y: 0, duration: 0.8 },
        0.45
      );
    }

    // Hero 3 Pillars Cards
    const heroPillars = document.querySelectorAll('[data-hero-pillar]');
    if (heroPillars.length > 0) {
      heroTl.fromTo(
        heroPillars,
        { opacity: 0, y: 22 },
        { opacity: 1, y: 0, stagger: 0.08, duration: 0.75 },
        0.55
      );
    }

    // Hero CTAs
    const heroCtas = document.querySelector('[data-hero-ctas]');
    if (heroCtas) {
      heroTl.fromTo(
        heroCtas,
        { opacity: 0, y: 15 },
        { opacity: 1, y: 0, duration: 0.7 },
        0.7
      );
    }

    // Right Column: Ficha de Garantía 3D Settle
    const guaranteeCard = document.getElementById('hero-guarantee-card');
    if (guaranteeCard) {
      heroTl.fromTo(
        guaranteeCard,
        { opacity: 0, x: 35, rotationY: -10, rotationX: 4 },
        {
          opacity: 1,
          x: 0,
          rotationY: 0,
          rotationX: 0,
          duration: 1.1,
          ease: 'power3.out',
        },
        0.35
      );
    }

    // -------------------------------------------------------------
    // B. INTERACTIVE 3D PERSPECTIVE TILT (via gsap.quickTo)
    // -------------------------------------------------------------
    const tiltCards = document.querySelectorAll<HTMLElement>('[data-tilt-card], #hero-guarantee-card');
    tiltCards.forEach((card) => {
      const rotXTo = gsap.quickTo(card, 'rotationX', { duration: 0.35, ease: 'power2.out' });
      const rotYTo = gsap.quickTo(card, 'rotationY', { duration: 0.35, ease: 'power2.out' });

      // Apply perspective on parent or self
      card.style.transformStyle = 'preserve-3d';
      if (card.parentElement) {
        card.parentElement.style.perspective = '1200px';
      }

      function onMouseMove(e: MouseEvent) {
        const rect = card.getBoundingClientRect();
        const x = e.clientX - rect.left;
        const y = e.clientY - rect.top;
        const xPercent = (x / rect.width - 0.5) * 2; // -1 to 1
        const yPercent = (y / rect.height - 0.5) * 2; // -1 to 1

        rotYTo(xPercent * 6); // Max 6 deg Y
        rotXTo(-yPercent * 4); // Max 4 deg X
      }

      function onMouseLeave() {
        rotXTo(0);
        rotYTo(0);
      }

      card.addEventListener('mousemove', onMouseMove);
      card.addEventListener('mouseleave', onMouseLeave);
    });

    // -------------------------------------------------------------
    // C. MAGNETIC BUTTONS (via gsap.quickTo)
    // -------------------------------------------------------------
    const magneticBtns = document.querySelectorAll<HTMLElement>('[data-magnetic-btn]');
    magneticBtns.forEach((btn) => {
      const xTo = gsap.quickTo(btn, 'x', { duration: 0.3, ease: 'power3.out' });
      const yTo = gsap.quickTo(btn, 'y', { duration: 0.3, ease: 'power3.out' });

      const icon = btn.querySelector<HTMLElement>('.magnetic-icon');
      const iconXTo = icon ? gsap.quickTo(icon, 'x', { duration: 0.35, ease: 'power3.out' }) : null;
      const iconYTo = icon ? gsap.quickTo(icon, 'y', { duration: 0.35, ease: 'power3.out' }) : null;

      function onMouseMove(e: MouseEvent) {
        const rect = btn.getBoundingClientRect();
        const x = e.clientX - (rect.left + rect.width / 2);
        const y = e.clientY - (rect.top + rect.height / 2);

        xTo(x * 0.32);
        yTo(y * 0.32);

        if (iconXTo && iconYTo) {
          iconXTo(x * 0.45);
          iconYTo(y * 0.45);
        }
      }

      function onMouseLeave() {
        gsap.to(btn, { x: 0, y: 0, duration: 0.55, ease: 'elastic.out(1, 0.4)' });
        if (icon) {
          gsap.to(icon, { x: 0, y: 0, duration: 0.55, ease: 'elastic.out(1, 0.4)' });
        }
      }

      btn.addEventListener('mousemove', onMouseMove);
      btn.addEventListener('mouseleave', onMouseLeave);
    });

    // -------------------------------------------------------------
    // D. TELEMETRY DIALS SCROLLTRIGGER REVEALS & COUNTERS
    // -------------------------------------------------------------
    const dialsGrid = document.querySelector('#garantias');
    if (dialsGrid) {
      // Stagger Dial Cards
      const dialCards = dialsGrid.querySelectorAll('[data-dial-card]');
      gsap.fromTo(
        dialCards,
        { opacity: 0, y: 35 },
        {
          opacity: 1,
          y: 0,
          scrollTrigger: {
            trigger: dialsGrid,
            start: 'top 78%',
            once: true,
          },
          stagger: 0.09,
          duration: 0.85,
          ease: 'power3.out',
        }
      );

      // Gauge Bars Animation
      const gauges = dialsGrid.querySelectorAll<HTMLElement>('[data-dial-gauge]');
      gauges.forEach((gauge) => {
        const targetWidth = gauge.getAttribute('data-dial-gauge') || '90%';
        gsap.fromTo(
          gauge,
          { width: '0%' },
          {
            width: targetWidth,
            duration: 1.3,
            ease: 'expo.out',
            scrollTrigger: {
              trigger: gauge,
              start: 'top 85%',
              once: true,
            },
          }
        );
      });

      // Metric Counter Tweens
      const counters = dialsGrid.querySelectorAll<HTMLElement>('[data-dial-counter]');
      counters.forEach((counter) => {
        const targetValue = parseFloat(counter.getAttribute('data-dial-counter') || '0');
        const decimals = parseInt(counter.getAttribute('data-dial-decimals') || '0', 10);
        const prefix = counter.getAttribute('data-dial-prefix') || '';
        const suffix = counter.getAttribute('data-dial-suffix') || '';

        const proxy = { val: 0 };
        gsap.to(proxy, {
          val: targetValue,
          duration: 1.4,
          ease: 'power2.out',
          scrollTrigger: {
            trigger: counter,
            start: 'top 85%',
            once: true,
          },
          onUpdate: () => {
            counter.textContent = `${prefix}${proxy.val.toFixed(decimals)}${suffix}`;
          },
        });
      });
    }

    // -------------------------------------------------------------
    // E. WAYBILL PACKAGES STAGGER & SIBLING SPOTLIGHT
    // -------------------------------------------------------------
    const packagesSection = document.querySelector('#paquetes');
    if (packagesSection) {
      const packageCards = packagesSection.querySelectorAll<HTMLElement>('[data-package-card]');
      gsap.fromTo(
        packageCards,
        { opacity: 0, y: 45 },
        {
          opacity: 1,
          y: 0,
          scrollTrigger: {
            trigger: packagesSection,
            start: 'top 75%',
            once: true,
          },
          stagger: 0.12,
          duration: 0.9,
          ease: 'power3.out',
        }
      );

      // Sibling Dimming on Hover
      packageCards.forEach((card) => {
        card.addEventListener('mouseenter', () => {
          packageCards.forEach((other) => {
            if (other !== card) {
              gsap.to(other, { opacity: 0.6, scale: 0.985, duration: 0.35, ease: 'power2.out' });
            } else {
              gsap.to(card, { y: -6, scale: 1.015, duration: 0.35, ease: 'power2.out' });
            }
          });
        });

        card.addEventListener('mouseleave', () => {
          packageCards.forEach((c) => {
            gsap.to(c, { opacity: 1, scale: 1, y: 0, duration: 0.35, ease: 'power2.out' });
          });
        });
      });
    }

    // -------------------------------------------------------------
    // F. CUCEA TERMINAL & COMPARISON ACCENT
    // -------------------------------------------------------------
    const cuceaSection = document.querySelector('#cucea');
    if (cuceaSection) {
      const cuceaCards = cuceaSection.querySelectorAll('[data-cucea-reveal]');
      gsap.fromTo(
        cuceaCards,
        { opacity: 0, y: 30 },
        {
          opacity: 1,
          y: 0,
          scrollTrigger: {
            trigger: cuceaSection,
            start: 'top 75%',
            once: true,
          },
          stagger: 0.1,
          duration: 0.85,
          ease: 'power3.out',
        }
      );
    }

    // -------------------------------------------------------------
    // G. AUDIT FORM WAYBILL REVEAL
    // -------------------------------------------------------------
    const auditSection = document.querySelector('#auditoria');
    if (auditSection) {
      const auditCard = auditSection.querySelector('#audit-waybill-card');
      if (auditCard) {
        gsap.fromTo(
          auditCard,
          { opacity: 0, scale: 0.98, y: 35 },
          {
            opacity: 1,
            scale: 1,
            y: 0,
            scrollTrigger: {
              trigger: auditSection,
              start: 'top 80%',
              once: true,
            },
            duration: 0.9,
            ease: 'power3.out',
          }
        );
      }
    }
  });

  // Fallback for reduced motion: ensure complete visibility
  mm.add('(prefers-reduced-motion: reduce)', () => {
    gsap.set(
      '[data-hero-badge], #hero-title, [data-hero-desc], [data-hero-pillar], #hero-guarantee-card, [data-dial-card], [data-package-card], [data-cucea-reveal], #audit-waybill-card',
      {
        opacity: 1,
        y: 0,
        scale: 1,
        rotationX: 0,
        rotationY: 0,
      }
    );
  });
}
