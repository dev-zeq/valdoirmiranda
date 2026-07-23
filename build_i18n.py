#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re, os

SRC = '/home/zeqmiranda/ValdoirMiranda/index.html'
full = open(SRC, encoding='utf-8').read()

# (pt, en, es) — text-node translations
TR = [
 ("Sobre","About","Sobre"),
 ("Áreas","Areas","Áreas"),
 ("Trajetória","Journey","Trayectoria"),
 ("Legado","Legacy","Legado"),
 ("O Código","The Code","El Código"),
 ("Investimento","Investment","Inversión"),
 ("Áreas de Estudo","Study Areas","Áreas de Estudio"),
 ("Pesquisador Independente","Independent Researcher","Investigador Independiente"),
 ("Por que tantas pessoas vivem sem energia,","Why do so many people live without energy,","¿Por qué tantas personas viven sin energía,"),
 ("mesmo comendo \"certo\"?","even when eating \"right\"?","incluso comiendo \"bien\"?"),
 ("Décadas de estudo sobre alimentação, corpo, mente e longevidade, reunidas por","Decades of study on nutrition, body, mind and longevity, brought together by","Décadas de estudio sobre alimentación, cuerpo, mente y longevidad, reunidas por"),
 ("O Código da Longevidade","The Longevity Code","El Código de la Longevidad"),
 ("— pesquisador independente — para você viver mais e melhor, com energia e saúde em cada década que vem pela frente.","— independent researcher — so you can live longer and better, with energy and health in every decade ahead.","— investigador independiente — para que vivas más y mejor, con energía y salud en cada década que viene."),
 ("Quero destravar o Código","I want to unlock the Code","Quiero desbloquear el Código"),
 ("Conhecer a trajetória","Discover the journey","Conocer la trayectoria"),
 ("Alimentação","Nutrition","Alimentación"),
 ("Vitalidade","Vitality","Vitalidad"),
 ("Décadas de estudo","Decades of study","Décadas de estudio"),
 ("Quem é Valdoir","Who is Valdoir","Quién es Valdoir"),
 ("Décadas de estudo,","Decades of study,","Décadas de estudio,"),
 ("uma missão clara.","one clear mission.","una misión clara."),
 ("Valdoir Barreto Miranda dedicou grande parte de sua vida ao estudo da","Valdoir Barreto Miranda dedicated much of his life to the study of","Valdoir Barreto Miranda dedicó gran parte de su vida al estudio de la"),
 ("alimentação","nutrition","alimentación"),
 (", da",", ",", la"),
 ("saúde física","physical health","salud física"),
 ("saúde mental","mental health","salud mental"),
 ("e dos hábitos que influenciam a qualidade de vida.","and the habits that influence quality of life.","y los hábitos que influyen en la calidad de vida."),
 ("Ao longo dos anos, reuniu observações, pesquisas, ideias e materiais educativos","Over the years, he gathered observations, research, ideas and educational materials","A lo largo de los años, reunió observaciones, investigaciones, ideas y materiales educativos"),
 ("com o objetivo de ajudar pessoas a enxergarem a saúde de forma mais consciente.","with the goal of helping people see health in a more conscious way.","con el objetivo de ayudar a las personas a ver la salud de forma más consciente."),
 ("Sua jornada começou com uma inquietação genuína: por que tantas pessoas","His journey began with a genuine restlessness: why do so many people","Su recorrido comenzó con una inquietud genuina: por qué tantas personas"),
 ("vivem sem energia, sem equilíbrio e sem clareza sobre o próprio corpo?","live without energy, without balance and without clarity about their own body?","viven sin energía, sin equilibrio y sin claridad sobre su propio cuerpo?"),
 ("Essa pergunta o guiou por décadas de leitura, observação e desenvolvimento","That question guided him through decades of reading, observation and development","Esa pregunta lo guió por décadas de lectura, observación y desarrollo"),
 ("de materiais educativos sobre","of educational materials on","de materiales educativos sobre"),
 ("longevidade","longevity","longevidad"),
 ("e","and","y"),
 ("vitalidade masculina","male vitality","vitalidad masculina"),
 ("Décadas","Decades","Décadas"),
 ("de estudo e pesquisa","of study and research","de estudio e investigación"),
 ("Áreas de estudo","Areas of study","Áreas de estudio"),
 ("Curiosidade pelo saber","Curiosity for knowledge","Curiosidad por el saber"),
 ("Missão: compartilhar","Mission: to share","Misión: compartir"),
 ('"A saúde não é um destino. É uma forma de caminhar — com escolhas conscientes,','"Health is not a destination. It is a way of walking — with conscious choices,','"La salud no es un destino. Es una forma de caminar — con decisiones conscientes,'),
 ('conhecimento e respeito pelo próprio corpo."','knowledge and respect for your own body."','conocimiento y respeto por el propio cuerpo."'),
 ("Abordagem","Approach","Enfoque"),
 ("Pesquisa independente, observação prática e integração de conhecimentos sobre saúde, corpo e bem-estar.","Independent research, practical observation and the integration of knowledge about health, body and well-being.","Investigación independiente, observación práctica e integración de conocimientos sobre salud, cuerpo y bienestar."),
 ("Propósito","Purpose","Propósito"),
 ("Organizar e compartilhar um acervo de décadas para que mais pessoas possam viver com mais energia, clareza e qualidade de vida.","Organize and share a decades-long collection so more people can live with more energy, clarity and quality of life.","Organizar y compartir un acervo de décadas para que más personas puedan vivir con más energía, claridad y calidad de vida."),
 ("O que Valdoir estuda","What Valdoir studies","Lo que Valdoir estudia"),
 ("Áreas de","Areas of","Áreas de"),
 ("Pesquisa","Research","Investigación"),
 ("Alimentação Inteligente","Smart Nutrition","Alimentación Inteligente"),
 ("Estudo sobre como os alimentos impactam a energia, o humor e o desempenho do organismo ao longo da vida.","A study of how food impacts energy, mood and the body's performance throughout life.","Estudio sobre cómo los alimentos impactan la energía, el ánimo y el desempeño del organismo a lo largo de la vida."),
 ("Combinação de Alimentos","Food Combining","Combinación de Alimentos"),
 ("Análise de como diferentes combinações alimentares afetam a digestão, absorção e bem-estar geral.","An analysis of how different food combinations affect digestion, absorption and overall well-being.","Análisis de cómo diferentes combinaciones de alimentos afectan la digestión, la absorción y el bienestar general."),
 ("Saúde Física","Physical Health","Salud Física"),
 ("Hábitos, movimentos e práticas que sustentam um corpo funcional, ativo e com mais disposição.","Habits, movements and practices that sustain a functional, active body with more energy.","Hábitos, movimientos y prácticas que sostienen un cuerpo funcional, activo y con más disposición."),
 ("Saúde Mental","Mental Health","Salud Mental"),
 ("Relação entre alimentação, rotina e equilíbrio emocional — o elo entre corpo saudável e mente tranquila.","The relationship between nutrition, routine and emotional balance — the link between a healthy body and a calm mind.","Relación entre alimentación, rutina y equilibrio emocional — el vínculo entre un cuerpo sano y una mente tranquila."),
 ("Vitalidade Masculina","Male Vitality","Vitalidad Masculina"),
 ("Estudo aprofundado sobre energia, hormônios, desempenho e bem-estar específico para o organismo masculino.","An in-depth study of energy, hormones, performance and well-being specific to the male body.","Estudio profundo sobre energía, hormonas, desempeño y bienestar específico para el organismo masculino."),
 ("Estudo aprofundado sobre hormônios, ciclo e bem-estar específico para o organismo feminino.","An in-depth study of hormones, cycle and well-being specific to the female body.","Estudio profundo sobre hormonas, ciclo y bienestar específico para el organismo femenino."),
 ("Longevidade","Longevity","Longevidad"),
 ("O que a ciência e a observação revelam sobre viver mais — com saúde, energia e qualidade.","What science and observation reveal about living longer — with health, energy and quality.","Lo que la ciencia y la observación revelan sobre vivir más — con salud, energía y calidad."),
 ("Estudos e Pesquisas","Studies & Research","Estudios e Investigaciones"),
 ("Materiais reunidos ao longo de décadas: leituras, observações e análises sobre saúde integrada.","Materials gathered over decades: readings, observations and analyses on integrated health.","Materiales reunidos a lo largo de décadas: lecturas, observaciones y análisis sobre salud integrada."),
 ("Qualidade de Vida","Quality of Life","Calidad de Vida"),
 ("Integração entre alimentação, saúde, propósito e hábitos para uma vida com mais plenitude e equilíbrio.","The integration of nutrition, health, purpose and habits for a life of greater fullness and balance.","Integración entre alimentación, salud, propósito y hábitos para una vida con más plenitud y equilibrio."),
 ("Uma jornada de décadas","A journey of decades","Una jornada de décadas"),
 ("A","The","La"),
 ("de Valdoir","of Valdoir","de Valdoir"),
 ("Início da Jornada","The Beginning","El Inicio del Recorrido"),
 ("Os primeiros estudos","The first studies","Los primeros estudios"),
 ("Valdoir começa a se interessar por alimentação e saúde, buscando respostas além do senso comum sobre como o corpo funciona e o que realmente influencia o bem-estar.","Valdoir starts to take an interest in nutrition and health, seeking answers beyond common sense about how the body works and what really influences well-being.","Valdoir comienza a interesarse por la alimentación y la salud, buscando respuestas más allá del sentido común sobre cómo funciona el cuerpo y qué influye realmente en el bienestar."),
 ("Anos de Pesquisa","Years of Research","Años de Investigación"),
 ("Observações independentes","Independent observations","Observaciones independientes"),
 ("Décadas de leitura, observação e registro. Cada novo aprendizado é anotado, testado e incorporado a uma visão cada vez mais ampla sobre saúde e qualidade de vida.","Decades of reading, observation and record-keeping. Each new lesson is noted, tested and incorporated into an ever-broader view of health and quality of life.","Décadas de lectura, observación y registro. Cada nuevo aprendizaje se anota, se prueba y se incorpora a una visión cada vez más amplia sobre salud y calidad de vida."),
 ("Desenvolvimento","Development","Desarrollo"),
 ("Foco na vitalidade masculina","Focus on male vitality","Enfoque en la vitalidad masculina"),
 ("Aprofundamento em estudos sobre energia, hormônios e bem-estar masculino, reconhecendo a carência de informação de qualidade nesta área.","A deeper dive into studies on energy, hormones and male well-being, recognizing the lack of quality information in this area.","Profundización en estudios sobre energía, hormonas y bienestar masculino, reconociendo la falta de información de calidad en esta área."),
 ("Produção","Production","Producción"),
 ("Criação dos materiais educativos","Creating the educational materials","Creación de los materiales educativos"),
 ("Mais de 50 guias, estudos e conteúdos desenvolvidos com o objetivo de compartilhar conhecimento de forma acessível, clara e responsável.","More than 50 guides, studies and pieces of content created to share knowledge in an accessible, clear and responsible way.","Más de 50 guías, estudios y contenidos desarrollados con el objetivo de compartir conocimiento de forma accesible, clara y responsable."),
 ("Presente e Futuro","Present & Future","Presente y Futuro"),
 ("Organização do acervo digital","Organizing the digital collection","Organización del acervo digital"),
 ("O legado de uma vida dedicada ao estudo ganha forma digital em O Código da Longevidade, para que este conhecimento alcance cada vez mais pessoas.","The legacy of a life devoted to study takes digital form in The Longevity Code, so this knowledge can reach more and more people.","El legado de una vida dedicada al estudio toma forma digital en El Código de la Longevidad, para que este conocimiento llegue a cada vez más personas."),
 ("O que fica","What remains","Lo que queda"),
 ("Um","A","Un"),
 ("de Conhecimento","of Knowledge","de Conocimiento"),
 ("Mais do que textos ou materiais, este acervo representa uma vida de","More than texts or materials, this collection represents a life of","Más que textos o materiales, este acervo representa una vida de"),
 ("curiosidade","curiosity","curiosidad"),
 ("dedicação","dedication","dedicación"),
 ("e desejo de compartilhar conhecimento.","and a desire to share knowledge.","y el deseo de compartir conocimiento."),
 ("Cada estudo carrega uma parte da trajetória de Valdoir e de sua visão sobre saúde,","Each study carries a part of Valdoir's journey and his vision of health,","Cada estudio lleva una parte de la trayectoria de Valdoir y de su visión sobre la salud,"),
 ("energia, corpo e mente. É um presente para quem busca entender melhor a si mesmo","energy, body and mind. It is a gift for those who seek to understand themselves better","energía, cuerpo y mente. Es un regalo para quien busca entenderse mejor a sí mismo"),
 ("e viver de forma mais consciente e plena.","and live in a more conscious and full way.","y vivir de forma más consciente y plena."),
 ("O acervo, por dentro","Inside the collection","El acervo, por dentro"),
 ("O","The","El"),
 ("Código da Longevidade","Longevity Code","Código de la Longevidad"),
 ("Décadas de estudo e observação estão sendo organizadas e reunidas em O Código da Longevidade.","Decades of study and observation are being organized and brought together in The Longevity Code.","Décadas de estudio y observación están siendo organizadas y reunidas en El Código de la Longevidad."),
 ("Os 6 primeiros módulos já estão disponíveis — guias, estudos e conteúdos sobre alimentação, saúde masculina,","The first 6 modules are already available — guides, studies and content on nutrition, male health,","Los primeros 6 módulos ya están disponibles — guías, estudios y contenidos sobre alimentación, salud masculina,"),
 ("equilíbrio físico e mental e longevidade. E quem entra agora recebe também tudo o que ainda vem.","physical and mental balance, and longevity. And whoever joins now also gets everything still to come.","equilibrio físico y mental y longevidad. Y quien entra ahora recibe también todo lo que aún viene."),
 ("📱 Funciona liso no celular","📱 Runs smoothly on your phone","📱 Funciona perfecto en el celular"),
 ("🎨 Visual moderno e intuitivo","🎨 Modern, intuitive design","🎨 Diseño moderno e intuitivo"),
 ("✅ Progresso salvo automaticamente","✅ Progress saved automatically","✅ Progreso guardado automáticamente"),
 ("Organização do acervo: 60% concluído","Collection progress: 60% complete","Organización del acervo: 60% completado"),
 ("O preço de fundador (R$ 37) vale até o acervo chegar a 100%","The founder price (R$ 37) is valid until the collection reaches 100%","El precio de fundador (R$ 37) es válido hasta que el acervo llegue al 100%"),
 ("Guia de Combinação dos Alimentos","Food Combining Guide","Guía de Combinación de Alimentos"),
 ("Como combinar alimentos de forma inteligente para melhorar a digestão e aumentar a energia disponível.","How to combine foods intelligently to improve digestion and increase available energy.","Cómo combinar alimentos de forma inteligente para mejorar la digestión y aumentar la energía disponible."),
 ("🔓 Incluído no acesso","🔓 Included in your access","🔓 Incluido en el acceso"),
 ("Energia","Energy","Energía"),
 ("Alimentação e Energia","Nutrition and Energy","Alimentación y Energía"),
 ("O que comer para manter o ânimo, o foco e a disposição ao longo do dia — e o que evitar.","What to eat to keep your mood, focus and energy up throughout the day — and what to avoid.","Qué comer para mantener el ánimo, el enfoque y la disposición durante el día — y qué evitar."),
 ("Masculinidade","Masculinity","Masculinidad"),
 ("Saúde Masculina e Vitalidade","Male Health and Vitality","Salud Masculina y Vitalidad"),
 ("Estudos sobre hormônios, energia e bem-estar específico para o organismo e a saúde do homem.","Studies on hormones, energy and well-being specific to the male body and men's health.","Estudios sobre hormonas, energía y bienestar específico para el organismo y la salud del hombre."),
 ("Equilíbrio","Balance","Equilibrio"),
 ("Corpo, Mente e Hábitos","Body, Mind and Habits","Cuerpo, Mente y Hábitos"),
 ("A conexão entre alimentação, hábitos diários e saúde mental — e como pequenas escolhas fazem grande diferença.","The connection between nutrition, daily habits and mental health — and how small choices make a big difference.","La conexión entre alimentación, hábitos diarios y salud mental — y cómo las pequeñas decisiones hacen una gran diferencia."),
 ("Longevidade e Qualidade de Vida","Longevity and Quality of Life","Longevidad y Calidad de Vida"),
 ("O que décadas de pesquisa revelam sobre viver mais — com saúde, propósito e bem-estar real.","What decades of research reveal about living longer — with health, purpose and real well-being.","Lo que décadas de investigación revelan sobre vivir más — con salud, propósito y bienestar real."),
 ("Vitalidade Feminina","Female Vitality","Vitalidad Femenina"),
 ("Estudos sobre hormônios, energia e bem-estar específico para o organismo e a saúde da mulher.","Studies on hormones, energy, and well-being specific to the female body and health.","Estudios sobre hormonas, energía y bienestar específico para el organismo y la salud de la mujer."),
 ("Mais materiais","More materials","Más materiales"),
 ("em breve","coming soon","próximamente"),
 ("Novos guias e estudos serão adicionados continuamente.","New guides and studies will be added continuously.","Se añadirán nuevas guías y estudios de forma continua."),
 ("Acesso ao","Access to the","Acceso al"),
 ("Um valor simbólico para tornar décadas de estudo acessíveis a quem realmente quer aprender —","A symbolic price to make decades of study accessible to those who truly want to learn —","Un valor simbólico para hacer accesibles décadas de estudio a quien realmente quiere aprender —"),
 ("hoje, e em tudo que ainda vai ser adicionado.","today, and in everything that will still be added.","hoy, y en todo lo que aún se va a añadir."),
 ("🚀 Oferta de Lançamento","🚀 Launch Offer","🚀 Oferta de Lanzamiento"),
 ("Preço de Fundador","Founder Price","Precio de Fundador"),
 ("de R$ 67","from R$ 67","de R$ 67"),
 ("por","for","por"),
 ("Pagamento único · sem mensalidades","One-time payment · no subscription","Pago único · sin mensualidades"),
 ("Preço em reais (R$) — convertido para a sua moeda no checkout.","Price in Brazilian reais (R$) — converted to your currency at checkout.","Precio en reales (R$) — convertido a tu moneda en el checkout."),
 ("✓ Os 5 módulos atuais de O Código da Longevidade","✓ The 5 current modules of The Longevity Code","✓ Los 5 módulos actuales de El Código de la Longevidad"),
 ("✓ Todo o conteúdo futuro incluído — sem pagar de novo","✓ All future content included — no extra payment","✓ Todo el contenido futuro incluido — sin pagar de nuevo"),
 ("✓ Acesso pela área de membros","✓ Access through the members' area","✓ Acceso por el área de miembros"),
 ("R$ 37 garantido para sempre","R$ 37 locked in forever","R$ 37 asegurado para siempre"),
 ("— o preço só sobe para quem entrar depois","— the price only goes up for those who join later","— el precio solo sube para quien entre después"),
 ("O valor sobe para","The price rises to","El valor sube a"),
 ("assim que o acervo completar 100% dos materiais","as soon as the collection reaches 100% of its materials","en cuanto el acervo complete el 100% de los materiales"),
 ("(hoje em 60%)","(today at 60%)","(hoy en 60%)"),
 (". Quem entra agora trava o preço de fundador para sempre.",". Whoever joins now locks in the founder price forever.",". Quien entra ahora fija el precio de fundador para siempre."),
 ("Quero meu acesso por R$ 37","I want my access for R$ 37","Quiero mi acceso por R$ 37"),
 ("Pagamento seguro via Hotmart · Acesso liberado automaticamente por e-mail","Secure payment via Hotmart · Access delivered automatically by email","Pago seguro vía Hotmart · Acceso liberado automáticamente por correo"),
 ("Garantia de 7 dias.","7-day guarantee.","Garantía de 7 días."),
 ("Se não fizer sentido pra você, é só pedir reembolso — sem burocracia.","If it's not right for you, just ask for a refund — no hassle.","Si no tiene sentido para ti, solo pide el reembolso — sin burocracia."),
 ("Aviso Educativo:","Educational Notice:","Aviso Educativo:"),
 ("Os conteúdos apresentados têm finalidade educativa e informativa.","The content presented is for educational and informational purposes.","Los contenidos presentados tienen finalidad educativa e informativa."),
 ("Eles não substituem acompanhamento médico, nutricional, psicológico ou qualquer tratamento profissional.","They do not replace medical, nutritional, psychological or any professional treatment.","No sustituyen el acompañamiento médico, nutricional, psicológico ni ningún tratamiento profesional."),
 ("Consulte sempre um profissional de saúde habilitado para orientações personalizadas.","Always consult a qualified health professional for personalized guidance.","Consulta siempre a un profesional de salud habilitado para orientaciones personalizadas."),
 ('"O conhecimento só tem valor quando é compartilhado."','"Knowledge only has value when it is shared."','"El conocimiento solo tiene valor cuando se comparte."'),
 ("O Código da Longevidade · por Valdoir Miranda · Pesquisa Independente em Saúde, Alimentação e Longevidade","The Longevity Code · by Valdoir Miranda · Independent Research in Health, Nutrition and Longevity","El Código de la Longevidad · por Valdoir Miranda · Investigación Independiente en Salud, Alimentación y Longevidad"),
 ("O Código da Longevidade — por Valdoir Miranda | Viver Mais, com Saúde e Energia","The Longevity Code — by Valdoir Miranda | Live Longer, with Health and Energy","El Código de la Longevidad — por Valdoir Miranda | Vive Más, con Salud y Energía"),
]

# Attribute-based head fields (direct string replace on full HTML)
HEAD = [
 # (pt, en, es)
 ('content="O que décadas de pesquisa revelam sobre viver mais — com saúde, energia e vitalidade. O Código da Longevidade reúne o acervo de estudos de Valdoir Miranda sobre alimentação, corpo, mente e longevidade. Acesso vitalício com preço de fundador."',
  'content="What decades of research reveal about living longer — with health, energy and vitality. The Longevity Code brings together Valdoir Miranda\'s collection of studies on nutrition, body, mind and longevity. Lifetime access at a founder price."',
  'content="Lo que décadas de investigación revelan sobre vivir más — con salud, energía y vitalidad. El Código de la Longevidad reúne el acervo de estudios de Valdoir Miranda sobre alimentación, cuerpo, mente y longevidad. Acceso vitalicio con precio de fundador."'),
 ('content="O Código da Longevidade — por Valdoir Miranda"',
  'content="The Longevity Code — by Valdoir Miranda"',
  'content="El Código de la Longevidad — por Valdoir Miranda"'),
 ('content="O que décadas de pesquisa revelam sobre viver mais — com saúde, energia e vitalidade. Décadas de estudo sobre alimentação, corpo, mente e longevidade, reunidas para você aplicar na sua vida."',
  'content="What decades of research reveal about living longer — with health, energy and vitality. Decades of study on nutrition, body, mind and longevity, brought together for you to apply in your life."',
  'content="Lo que décadas de investigación revelan sobre vivir más — con salud, energía y vitalidad. Décadas de estudio sobre alimentación, cuerpo, mente y longevidad, reunidas para que las apliques en tu vida."'),
 ('content="pt_BR"', 'content="en_US"', 'content="es_ES"'),
]

# multi-line nodes: groups of pt fragments that are actually ONE text node
MERGES = [
 ["e dos hábitos que influenciam a qualidade de vida.","Ao longo dos anos, reuniu observações, pesquisas, ideias e materiais educativos","com o objetivo de ajudar pessoas a enxergarem a saúde de forma mais consciente."],
 ["Sua jornada começou com uma inquietação genuína: por que tantas pessoas","vivem sem energia, sem equilíbrio e sem clareza sobre o próprio corpo?","Essa pergunta o guiou por décadas de leitura, observação e desenvolvimento","de materiais educativos sobre"],
 ['"A saúde não é um destino. É uma forma de caminhar — com escolhas conscientes,','conhecimento e respeito pelo próprio corpo."'],
 ["e desejo de compartilhar conhecimento.","Cada estudo carrega uma parte da trajetória de Valdoir e de sua visão sobre saúde,","energia, corpo e mente. É um presente para quem busca entender melhor a si mesmo","e viver de forma mais consciente e plena."],
 ["Décadas de estudo e observação estão sendo organizadas e reunidas em O Código da Longevidade.","Os 6 primeiros módulos já estão disponíveis — guias, estudos e conteúdos sobre alimentação, saúde masculina,","equilíbrio físico e mental e longevidade. E quem entra agora recebe também tudo o que ainda vem."],
 ["Um valor simbólico para tornar décadas de estudo acessíveis a quem realmente quer aprender —","hoje, e em tudo que ainda vai ser adicionado."],
 ["Os conteúdos apresentados têm finalidade educativa e informativa.","Eles não substituem acompanhamento médico, nutricional, psicológico ou qualquer tratamento profissional.","Consulte sempre um profissional de saúde habilitado para orientações personalizadas."],
]

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

def translate(full, idx, lang_attr, active_class):
    # protect script and style blocks
    store = []
    def stash(m):
        store.append(m.group(0)); return "\x00%d\x00" % (len(store)-1)
    text = re.sub(r'<script.*?</script>|<style.*?</style>', stash, full, flags=re.S|re.I)

    # head attribute replacements
    for row in HEAD:
        pt = row[0]; tr = row[idx]
        if pt not in text:
            print("  WARN head no-match:", pt[:50])
        text = text.replace(pt, tr)

    # html lang
    text = text.replace('<html lang="pt-BR">', '<html lang="%s">' % lang_attr)

    # build translation dict (normalized keys)
    D = {norm(row[0]): row[idx] for row in TR}
    # merged multi-line nodes: join fragment translations with a space
    for frags in MERGES:
        key = norm(' '.join(frags))
        val = ' '.join(D[norm(f)] for f in frags)
        for f in frags:
            D.pop(norm(f), None)
        D[key] = val

    tokens = re.split(r'(<[^>]+>)', text)
    unmatched = set(D.keys())
    for i in range(0, len(tokens), 2):
        seg = tokens[i]
        key = norm(seg)
        if key in D:
            lead = seg[:len(seg)-len(seg.lstrip())]
            trail = seg[len(seg.rstrip()):]
            tokens[i] = lead + D[key] + trail
            unmatched.discard(key)
    text = ''.join(tokens)
    for u in unmatched:
        print("  WARN text no-match:", repr(u[:55]))

    # restore protected
    def unstash(m): return store[int(m.group(1))]
    text = re.sub("\x00(\\d+)\x00", unstash, text)

    # active language in switcher
    text = text.replace('class="lang-pt active"', 'class="lang-pt"')
    text = text.replace('class="%s"' % active_class, 'class="%s active"' % active_class)
    return text

print("== EN ==")
en = translate(full, 1, "en", "lang-en")
os.makedirs('/home/zeqmiranda/ValdoirMiranda/en', exist_ok=True)
open('/home/zeqmiranda/ValdoirMiranda/en/index.html','w',encoding='utf-8').write(en)

print("== ES ==")
es = translate(full, 2, "es-419", "lang-es")
os.makedirs('/home/zeqmiranda/ValdoirMiranda/es', exist_ok=True)
open('/home/zeqmiranda/ValdoirMiranda/es/index.html','w',encoding='utf-8').write(es)

print("done")
