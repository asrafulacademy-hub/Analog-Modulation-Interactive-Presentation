import re

path = r"c:\Users\Apollo Gadget\OneDrive\Desktop\Analog-to-Analog Conversion\index.html"
with open(path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Replace Presenter Avatar box 'AI' with academic student graduation cap SVG
cap_svg = '<div class="presenter-avatar-box" title="Student Presenter"><svg width="32" height="32" viewBox="0 0 24 24" fill="#070d18"><path d="M12 3L1 9L12 15L21 10.09V17H23V9M5 13.18V17.18L12 21L19 17.18V13.18L12 17L5 13.18Z"/></svg></div>'
html = html.replace('<div class="presenter-avatar-box">AI</div>', cap_svg)

# 2. Humanize titles and text
html = html.replace('Presenter Teleprompter', 'Presenter Notes (Lecture Script)')
html = html.replace('Interactive Educational Simulation · 100% Offline', 'Lecture 08 Visual Demonstration · CSE, University of Barishal')
html = html.replace('The Inefficiency Paradox', 'AM Transmitter Power Distribution')
html = html.replace('Final Examination Performance', 'Lecture 08 Quiz Summary')
html = html.replace('Outstanding Academic Mastery!', 'Great Score! Excellent Understanding')

# 3. Slide 2: Roadmap math
html = html.replace('($\\lambda/4$)', '<span class="math">(&lambda;/4)</span>')
html = html.replace('($2f_m$)', '<span class="math">(2<var>f</var><sub>m</sub>)</span>')
html = html.replace('($P_t = P_c(1 + m^2/2)$)', '<span class="math"><var>P</var><sub>t</sub> = <var>P</var><sub>c</sub>(1 + <var>m</var><sup>2</sup>/2)</span>')
html = html.replace('($\\beta = \\Delta f/f_m$)', '<span class="math">&beta; = &Delta;<var>f</var>/<var>f</var><sub>m</sub></span>')
html = html.replace('($dm/dt$)', '<span class="math">d<var>m</var>/d<var>t</var></span>')

# 4. Slide 3: Quarter wave antenna formula & text
s3_old_math = '<div class="formula-math">L_{antenna} \\approx \\frac{\\lambda}{4} = \\frac{c}{4 \\cdot f}</div>'
s3_new_math = '''<div class="formula-math">
  <span class="math"><var>L</var><sub>antenna</sub> &approx; <span class="math-frac"><span class="math-num">&lambda;</span><span class="math-den">4</span></span> = <span class="math-frac"><span class="math-num"><var>c</var></span><span class="math-den">4 &middot; <var>f</var></span></span></span>
</div>'''
html = html.replace(s3_old_math, s3_new_math)

html = html.replace('$c = 3 \\times 10^8\\text{ m/s}$', '<span class="math"><var>c</var> = 3 &times; 10<sup>8</sup> m/s</span>')
html = html.replace('$f$', '<span class="math"><var>f</var></span>')
html = html.replace('$\\lambda = \\frac{3 \\times 10^8}{10^3} = 300\\text{ km} \\implies \\mathbf{L = 75\\text{ km}}$', '<span class="math">&lambda; = 300 km &implies; <strong>L = 75 km</strong></span>')
html = html.replace('$\\lambda = \\frac{3 \\times 10^8}{10^8} = 3\\text{ m} \\implies \\mathbf{L = 75\\text{ cm}}$', '<span class="math">&lambda; = 3 m &implies; <strong>L = 75 cm</strong></span>')
html = html.replace('($f_{c1}, f_{c2}, f_{c3}$)', '<span class="math">(<var>f</var><sub>c1</sub>, <var>f</var><sub>c2</sub>, <var>f</var><sub>c3</sub>)</span>')

# 5. Slide 4: Carrier wave equation
s4_old_math = '<div class="formula-math">c(t) = A_c \\cos(2\\pi f_c t + \\phi)</div>'
s4_new_math = '''<div class="formula-math">
  <span class="math"><var>c</var>(<var>t</var>) = <var>A</var><sub>c</sub> cos(2&pi;<var>f</var><sub>c</sub><var>t</var> + &phi;)</span>
</div>'''
html = html.replace(s4_old_math, s4_new_math)
html = html.replace('$m(t)$', '<span class="math"><var>m</var>(<var>t</var>)</span>')
html = html.replace('$A_c$', '<span class="math"><var>A</var><sub>c</sub></span>')
html = html.replace('$f_c$', '<span class="math"><var>f</var><sub>c</sub></span>')
html = html.replace('$\\phi$', '<span class="math">&phi;</span>')
html = html.replace('$s(t) = A_c [1 + m \\cdot m(t)] \\cos(2\\pi f_c t)$', '<span class="math"><var>s</var>(<var>t</var>) = <var>A</var><sub>c</sub> [1 + <var>m</var>&middot;<var>m</var>(<var>t</var>)] cos(2&pi;<var>f</var><sub>c</sub><var>t</var>)</span>')
html = html.replace('$f(t) = f_c + \\Delta f \\cdot m(t)$', '<span class="math"><var>f</var>(<var>t</var>) = <var>f</var><sub>c</sub> + &Delta;<var>f</var>&middot;<var>m</var>(<var>t</var>)</span>')
html = html.replace('$s(t) = A_c \\cos(2\\pi f_c t + k_p \\cdot m(t))$', '<span class="math"><var>s</var>(<var>t</var>) = <var>A</var><sub>c</sub> cos(2&pi;<var>f</var><sub>c</sub><var>t</var> + <var>k</var><sub>p</sub>&middot;<var>m</var>(<var>t</var>))</span>')

# 6. Slide 5: AM Time domain equation
s5_old_math = '<div class="formula-math">s(t) = A_c [1 + m \\cdot \\cos(2\\pi f_m t)] \\cdot \\cos(2\\pi f_c t)</div>'
s5_new_math = '''<div class="formula-math">
  <span class="math"><var>s</var>(<var>t</var>) = <var>A</var><sub>c</sub> [1 + <var>m</var> cos(2&pi;<var>f</var><sub>m</sub><var>t</var>)] &middot; cos(2&pi;<var>f</var><sub>c</sub><var>t</var>)</span>
</div>'''
html = html.replace(s5_old_math, s5_new_math)
html = html.replace('<strong>$A_c$:</strong>', '<strong><span class="math"><var>A</var><sub>c</sub></span>:</strong>')
html = html.replace('<strong>$m$:</strong>', '<strong><span class="math"><var>m</var></span>:</strong>')
html = html.replace('$0 \\le m \\le 1$', '<span class="math">0 &le; <var>m</var> &le; 1</span>')
html = html.replace('<strong>$f_m$:</strong>', '<strong><span class="math"><var>f</var><sub>m</sub></span>:</strong>')
html = html.replace('<strong>$f_c$:</strong>', '<strong><span class="math"><var>f</var><sub>c</sub></span>:</strong>')
html = html.replace('$f_c \\gg f_m$', '<span class="math"><var>f</var><sub>c</sub> &gg; <var>f</var><sub>m</sub></span>')
html = html.replace('$[1 + m \\cdot m(t)]$', '<span class="math">[1 + <var>m</var>&middot;<var>m</var>(<var>t</var>)]</span>')

# 7. Slide 6: Modulation Index equation
s6_old_math = '<div class="formula-math">m = \\frac{A_{max} - A_{min}}{A_{max} + A_{min}} = \\frac{A_m}{A_c}</div>'
s6_new_math = '''<div class="formula-math">
  <span class="math"><var>m</var> = <span class="math-frac"><span class="math-num"><var>A</var><sub>max</sub> &minus; <var>A</var><sub>min</sub></span><span class="math-den"><var>A</var><sub>max</sub> + <var>A</var><sub>min</sub></span></span> = <span class="math-frac"><span class="math-num"><var>A</var><sub>m</sub></span><span class="math-den"><var>A</var><sub>c</sub></span></span></span>
</div>'''
html = html.replace(s6_old_math, s6_new_math)
html = html.replace('$A_{max}$', '<span class="math"><var>A</var><sub>max</sub></span>')
html = html.replace('$A_{min}$', '<span class="math"><var>A</var><sub>min</sub></span>')
html = html.replace('<strong>$m < 1$', '<strong><span class="math"><var>m</var> &lt; 1</span>')
html = html.replace('<strong>$m = 1$', '<strong><span class="math"><var>m</var> = 1</span>')
html = html.replace('<strong>$m > 1$', '<strong><span class="math"><var>m</var> &gt; 1</span>')

# 8. Slide 7: AM Bandwidth
s7_old_math = '<div class="formula-math">B_{AM} = (f_c + f_m) - (f_c - f_m) = 2 f_m = 2 B</div>'
s7_new_math = '''<div class="formula-math">
  <span class="math"><var>B</var><sub>AM</sub> = (<var>f</var><sub>c</sub> + <var>f</var><sub>m</sub>) &minus; (<var>f</var><sub>c</sub> &minus; <var>f</var><sub>m</sub>) = 2<var>f</var><sub>m</sub> = 2<var>B</var></span>
</div>'''
html = html.replace(s7_old_math, s7_new_math)
html = html.replace('($f_c$)', '<span class="math">(<var>f</var><sub>c</sub>)</span>')
html = html.replace('$f_c - B$', '<span class="math"><var>f</var><sub>c</sub> &minus; <var>B</var></span>')
html = html.replace('$f_c + B$', '<span class="math"><var>f</var><sub>c</sub> + <var>B</var></span>')
html = html.replace('($B_{SSB} = B$)', '<span class="math">(<var>B</var><sub>SSB</sub> = <var>B</var>)</span>')

# 9. Slide 8: Worked examples
html = html.replace('$A_{max} = 10\\text{ V}$, $A_{min} = 2\\text{ V}$', '<span class="math"><var>A</var><sub>max</sub> = 10 V, <var>A</var><sub>min</sub> = 2 V</span>')
html = html.replace('<div class="step-calc">m = \\frac{A_{max} - A_{min}}{A_{max} + A_{min}} = \\frac{10 - 2}{10 + 2} = \\frac{8}{12} \\approx 0.67</div>',
                    '<div class="step-calc"><span class="math"><var>m</var> = <span class="math-frac"><span class="math-num">10 &minus; 2</span><span class="math-den">10 + 2</span></span> = <span class="math-frac"><span class="math-num">8</span><span class="math-den">12</span></span> &approx; 0.67 (67%)</span></div>')
html = html.replace('$B = 5\\text{ kHz}$', '<span class="math"><var>B</var> = 5 kHz</span>')
html = html.replace('$f_c = 1,000\\text{ kHz}$', '<span class="math"><var>f</var><sub>c</sub> = 1,000 kHz</span>')
html = html.replace('<div class="step-calc">B_{AM} = 2B = 2 \\times 5\\text{ kHz} = 10\\text{ kHz}</div>',
                    '<div class="step-calc"><span class="math"><var>B</var><sub>AM</sub> = 2<var>B</var> = 2 &times; 5 kHz = 10 kHz</span></div>')
html = html.replace('$1,000 \\pm 5\\text{ kHz} \\implies 995\\text{ kHz to } 1,005\\text{ kHz}$',
                    '<span class="math">1,000 &plusmn; 5 kHz &implies; 995 kHz to 1,005 kHz</span>')
html = html.replace('$1,170\\text{ kHz}$', '<span class="math">1,170 kHz</span>')
html = html.replace('<div class="step-calc">N_{channels} = \\frac{1,700 - 530}{10} = \\frac{1,170}{10} = \\mathbf{117\\text{ channels}}</div>',
                    '<div class="step-calc"><span class="math"><var>N</var><sub>channels</sub> = <span class="math-frac"><span class="math-num">1,700 &minus; 530</span><span class="math-den">10</span></span> = <span class="math-frac"><span class="math-num">1,170</span><span class="math-den">10</span></span> = <strong>117 channels</strong></span></div>')
html = html.replace('<div class="step-calc">N_{channels} = \\frac{1,602 - 531}{9} + 1 = \\mathbf{119\\text{ channels}}</div>',
                    '<div class="step-calc"><span class="math"><var>N</var><sub>channels</sub> = <span class="math-frac"><span class="math-num">1,602 &minus; 531</span><span class="math-den">9</span></span> + 1 = <strong>119 channels</strong></span></div>')

# 10. Slide 9: AM Power
s9_old_math = '<div class="formula-math">P_t = P_c \\left(1 + \\frac{m^2}{2}\\right) = P_c + P_{LSB} + P_{USB}</div>'
s9_new_math = '''<div class="formula-math">
  <span class="math"><var>P</var><sub>t</sub> = <var>P</var><sub>c</sub> (1 + <span class="math-frac"><span class="math-num"><var>m</var><sup>2</sup></span><span class="math-den">2</span></span>) = <var>P</var><sub>c</sub> + <var>P</var><sub>LSB</sub> + <var>P</var><sub>USB</sub></span>
</div>'''
html = html.replace(s9_old_math, s9_new_math)
html = html.replace('$P_{LSB} = P_{USB} = P_c \\cdot \\frac{m^2}{4}$', '<span class="math"><var>P</var><sub>LSB</sub> = <var>P</var><sub>USB</sub> = <var>P</var><sub>c</sub> &middot; <span class="math-frac"><span class="math-num"><var>m</var><sup>2</sup></span><span class="math-den">4</span></span></span>')
html = html.replace('$P_{sb} = P_c \\cdot \\frac{m^2}{2}$', '<span class="math"><var>P</var><sub>sb</sub> = <var>P</var><sub>c</sub> &middot; <span class="math-frac"><span class="math-num"><var>m</var><sup>2</sup></span><span class="math-den">2</span></span></span>')
html = html.replace('$P_c = 100\\text{ W}$, Modulation index $m = 0.8$', '<span class="math"><var>P</var><sub>c</sub> = 100 W, <var>m</var> = 0.8</span>')
html = html.replace('<div class="step-calc">P_t = 100 \\times \\left(1 + \\frac{0.8^2}{2}\\right) = 100 \\times (1 + 0.32) = \\mathbf{132\\text{ W}}</div>',
                    '<div class="step-calc"><span class="math"><var>P</var><sub>t</sub> = 100 &times; (1 + <span class="math-frac"><span class="math-num">0.8<sup>2</sup></span><span class="math-den">2</span></span>) = 100 &times; 1.32 = <strong>132 W</strong></span></div>')
html = html.replace('<div class="step-calc">P_{sb} = 132 - 100 = \\mathbf{32\\text{ W}} \\implies \\text{Efficiency} = \\frac{32}{132} \\approx \\mathbf{24.2\\%}</div>',
                    '<div class="step-calc"><span class="math"><var>P</var><sub>sb</sub> = 132 &minus; 100 = 32 W &implies; Efficiency = <span class="math-frac"><span class="math-num">32</span><span class="math-den">132</span></span> &approx; <strong>24.2%</strong></span></div>')
html = html.replace('($m=1$)', '<span class="math">(<var>m</var> = 1)</span>')

# 11. Slide 11: FM
s11_old_math = '<div class="formula-math">f(t) = f_c + \\Delta f \\cdot m(t)</div>'
s11_new_math = '''<div class="formula-math">
  <span class="math"><var>f</var>(<var>t</var>) = <var>f</var><sub>c</sub> + &Delta;<var>f</var> &middot; <var>m</var>(<var>t</var>)</span>
</div>'''
html = html.replace(s11_old_math, s11_new_math)
html = html.replace('$\\mathbf{\\beta = \\frac{\\Delta f}{f_m}}$', '<span class="math"><strong>&beta; = <span class="math-frac"><span class="math-num">&Delta;<var>f</var></span><span class="math-den"><var>f</var><sub>m</sub></span></span></strong></span>')
html = html.replace('$f_c + \\Delta f$', '<span class="math"><var>f</var><sub>c</sub> + &Delta;<var>f</var></span>')
html = html.replace('$f_c - \\Delta f$', '<span class="math"><var>f</var><sub>c</sub> &minus; &Delta;<var>f</var></span>')

# 12. Slide 12: Carson
s12_old_math = '<div class="formula-math">B_{FM} \\approx 2(\\Delta f + f_m) = 2(1 + \\beta)f_m</div>'
s12_new_math = '''<div class="formula-math">
  <span class="math"><var>B</var><sub>FM</sub> &approx; 2(&Delta;<var>f</var> + <var>f</var><sub>m</sub>) = 2(1 + &beta;)<var>f</var><sub>m</sub></span>
</div>'''
html = html.replace(s12_old_math, s12_new_math)
html = html.replace('$\\beta = 4$', '<span class="math">&beta; = 4</span>')
html = html.replace('$J_n(\\beta)$', '<span class="math"><var>J</var><sub>n</sub>(&beta;)</span>')
html = html.replace('$f_c \\pm f_m, f_c \\pm 2f_m, f_c \\pm 3f_m, \\dots$', '<span class="math"><var>f</var><sub>c</sub> &plusmn; <var>f</var><sub>m</sub>, <var>f</var><sub>c</sub> &plusmn; 2<var>f</var><sub>m</sub>, <var>f</var><sub>c</sub> &plusmn; 3<var>f</var><sub>m</sub>, &hellip;</span>')
html = html.replace('$|J_n(\\beta)|$', '<span class="math">|<var>J</var><sub>n</sub>(&beta;)|</span>')
html = html.replace('$n = \\beta + 1$', '<span class="math"><var>n</var> = &beta; + 1</span>')
html = html.replace('$\\beta \\implies$', '<span class="math">&beta;</span> &implies;')

# 13. Slide 13: FM Calculations
html = html.replace('$\\Delta f = 50\\text{ kHz}$, $f_m = 10\\text{ kHz}$', '<span class="math">&Delta;<var>f</var> = 50 kHz, <var>f</var><sub>m</sub> = 10 kHz</span>')
html = html.replace('<div class="step-calc">\\beta = \\frac{\\Delta f}{f_m} = \\frac{50\\text{ kHz}}{10\\text{ kHz}} = \\mathbf{5.0}</div>',
                    '<div class="step-calc"><span class="math">&beta; = <span class="math-frac"><span class="math-num">&Delta;<var>f</var></span><span class="math-den"><var>f</var><sub>m</sub></span></span> = <span class="math-frac"><span class="math-num">50 kHz</span><span class="math-den">10 kHz</span></span> = <strong>5.0</strong></span></div>')
html = html.replace('<div class="step-calc">B_{FM} = 2(\\Delta f + f_m) = 2(50 + 10) = 2 \\times 60 = \\mathbf{120\\text{ kHz}}</div>',
                    '<div class="step-calc"><span class="math"><var>B</var><sub>FM</sub> = 2(&Delta;<var>f</var> + <var>f</var><sub>m</sub>) = 2(50 + 10) = 2 &times; 60 = <strong>120 kHz</strong></span></div>')
html = html.replace('$2(1 + \\beta)f_m = 2(1 + 5) \\times 10 = 120\\text{ kHz}$',
                    '<span class="math">2(1 + &beta;)<var>f</var><sub>m</sub> = 2(1 + 5) &times; 10 = 120 kHz</span>')
html = html.replace('$f_m = 15\\text{ kHz}$, $\\beta = 4$', '<span class="math"><var>f</var><sub>m</sub> = 15 kHz, &beta; = 4</span>')
html = html.replace('<div class="step-calc">B_{FM} = 2(1 + 4) \\times 15\\text{ kHz} = 10 \\times 15 = \\mathbf{150\\text{ kHz}}</div>',
                    '<div class="step-calc"><span class="math"><var>B</var><sub>FM</sub> = 2(1 + 4) &times; 15 kHz = 10 &times; 15 = <strong>150 kHz</strong></span></div>')
html = html.replace('<div class="step-calc">N_{channels} = \\frac{108 - 88\\text{ MHz}}{0.2\\text{ MHz}} = \\frac{20}{0.2} = \\mathbf{100\\text{ channels}}</div>',
                    '<div class="step-calc"><span class="math"><var>N</var><sub>channels</sub> = <span class="math-frac"><span class="math-num">108 &minus; 88 MHz</span><span class="math-den">0.2 MHz</span></span> = <span class="math-frac"><span class="math-num">20</span><span class="math-den">0.2</span></span> = <strong>100 channels</strong></span></div>')
html = html.replace('$\\pm V_{limit}$', '<span class="math">&plusmn;<var>V</var><sub>limit</sub></span>')

# 14. Slide 15: PM
s15_old_math = '<div class="formula-math">s(t) = A_c \\cos(2\\pi f_c t + k_p \\cdot m(t))</div>'
s15_new_math = '''<div class="formula-math">
  <span class="math"><var>s</var>(<var>t</var>) = <var>A</var><sub>c</sub> cos(2&pi;<var>f</var><sub>c</sub><var>t</var> + <var>k</var><sub>p</sub>&middot;<var>m</var>(<var>t</var>))</span>
</div>'''
html = html.replace(s15_old_math, s15_new_math)
s15_deriv_old = '<div style=\"font-family:monospace; font-size:14px; color:var(--accent-cyan); background:rgba(0,0,0,0.3); padding:8px 12px; border-radius:6px; margin:4px 0;\">\n                  f_i(t) = \\frac{1}{2\\pi} \\frac{d\\theta}{dt} = f_c + \\frac{k_p}{2\\pi} \\cdot \\frac{dm(t)}{dt}\n                </div>'
s15_deriv_new = '''<div style="background:rgba(0,0,0,0.3); padding:8px 12px; border-radius:6px; margin:4px 0; text-align:center;">
  <span class="math"><var>f</var><sub>i</sub>(<var>t</var>) = <span class="math-frac"><span class="math-num">1</span><span class="math-den">2&pi;</span></span> <span class="math-frac"><span class="math-num">d&theta;</span><span class="math-den">d<var>t</var></span></span> = <var>f</var><sub>c</sub> + <span class="math-frac"><span class="math-num"><var>k</var><sub>p</sub></span><span class="math-den">2&pi;</span></span> &middot; <span class="math-frac"><span class="math-num">d<var>m</var>(<var>t</var>)</span><span class="math-den">d<var>t</var></span></span></span>
</div>'''
html = html.replace(s15_deriv_old, s15_deriv_new)
html = html.replace('$\\frac{dm}{dt} = 0 \\implies$', '<span class="math"><span class="math-frac"><span class="math-num">d<var>m</var></span><span class="math-den">d<var>t</var></span></span> = 0</span> &implies;')
html = html.replace('$\\frac{dm}{dt}$ is maximum $\\implies$', '<span class="math"><span class="math-frac"><span class="math-num">d<var>m</var></span><span class="math-den">d<var>t</var></span></span></span> is maximum &implies;')
html = html.replace('$B_{PM} \\approx 2(1 + \\beta)B$', '<span class="math"><var>B</var><sub>PM</sub> &approx; 2(1 + &beta;)<var>B</var></span>')

# 15. Slide 16 table
html = html.replace('$A_c$', '<span class="math"><var>A</var><sub>c</sub></span>')
html = html.replace('$f_c$', '<span class="math"><var>f</var><sub>c</sub></span>')
html = html.replace('$\\phi$', '<span class="math">&phi;</span>')
html = html.replace('$B = 2B$ (Narrow: $10\\text{ kHz}$)', '<span class="math"><var>B</var> = 2<var>B</var></span> (10 kHz)')
html = html.replace('$2(1 + \\beta)B$ with $\\beta \\approx 4\\text{--}5$ (Wide: $150\\text{--}200\\text{ kHz}$)', '<span class="math">2(1 + &beta;)<var>B</var></span> (&beta; &approx; 4&ndash;5, 150&ndash;200 kHz)')
html = html.replace('$2(1 + \\beta)B$ with $\\beta \\approx 1\\text{--}3$ (Moderate)', '<span class="math">2(1 + &beta;)<var>B</var></span> (&beta; &approx; 1&ndash;3)')
html = html.replace('$P_c$', '<span class="math"><var>P</var><sub>c</sub></span>')

# 16. Slide 17 & 19 & 20 & 21
html = html.replace('$\\frac{dm}{dt}$', '<span class="math">d<var>m</var>/d<var>t</var></span>')
html = html.replace('$\\tau = RC$', '<span class="math">&tau; = <var>RC</var></span>')
html = html.replace('$\\frac{1}{f_c} \\ll RC \\ll \\frac{1}{f_m}$', '<span class="math"><span class="math-frac"><span class="math-num">1</span><span class="math-den"><var>f</var><sub>c</sub></span></span> &ll; <var>RC</var> &ll; <span class="math-frac"><span class="math-num">1</span><span class="math-den"><var>f</var><sub>m</sub></span></span></span>')
html = html.replace('($\\tau = RC$)', '<span class="math">(&tau; = <var>RC</var>)</span>')
html = html.replace('($\\tau$)', '<span class="math">(&tau;)</span>')
html = html.replace('$f_{c1}$', '<span class="math"><var>f</var><sub>c1</sub></span>')
html = html.replace('$f_{c2}$', '<span class="math"><var>f</var><sub>c2</sub></span>')
html = html.replace('$f_{c3}$', '<span class="math"><var>f</var><sub>c3</sub></span>')

# 17. Clean up any remaining isolated dollar signs or raw backslashes
html = re.sub(r'\$([a-zA-Z0-9_\^\+\-\(\)\\/ ]+)\$', r'<span class="math">\1</span>', html)

with open(path, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated index.html with clean, robust HTML math typography and natural academic tone!")
