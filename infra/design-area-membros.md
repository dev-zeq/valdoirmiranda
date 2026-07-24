# Identidade visual da área de membros (mockup verde-profundo + dourado)

_Referência: mockup "Redescubra o prazer de se sentir bem" (24/07/2026). Aplicado nos 18 módulos (PT/ES/EN) neste repo. Este arquivo é o guia pra aplicar o MESMO visual no `/biblioteca` e nas páginas `/entrar` do `server.js` (que vive só na VPS, em `/opt/biblioteca-app`)._

## Tokens (copiar como estão nos módulos)

```css
:root{
  --serif: 'Cormorant Garamond', Georgia, 'Times New Roman', serif;
  --sans: 'DM Sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
  --brand-bg: #17342a;         /* verde profundo — header e bottom-nav, nos DOIS temas */
  --brand-bg-deep: #122a21;
  --brand-gold: #cfa963;       /* dourado champagne — logo, títulos do header, ícones */
  --brand-gold-strong: #e6c98f;/* dourado forte — item ativo do nav */
  --brand-gold-line: rgba(207,169,99,0.32); /* bordas/divisórias sobre verde */
  --brand-cream: #f0e8d2;      /* texto claro sobre verde */
}
html[data-theme="light"]{
  --bg: #f5f1e6; --bg-elevated: #fdfbf4; --bg-soft: #ece6d4;
  --text: #212b21; --text-soft: #5b695a; --border: #ded6bf;
  --heading: #1e3b2c;
  --accent: #96762f; --accent-strong: #6d5520; --accent-bg: #f1e8cf;
  --green: #1e4634; --green-bg: #e4ece2;
  --shadow: 0 10px 30px -12px rgba(30,59,44,0.18);
}
html[data-theme="dark"]{
  --bg: #0f231b; --bg-elevated: #173125; --bg-soft: #1c392b;
  --text: #eae4d2; --text-soft: #a5b4a1; --border: #2b4a38;
  --heading: #e9dfc2;
  --accent: #cfa963; --accent-strong: #e6c98f; --accent-bg: #29391f;
  --green: #8fc7a5; --green-bg: #1a3d2a;
  --shadow: 0 10px 34px -10px rgba(0,0,0,0.55);
}
```

Fontes (no `<head>`):

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:wght@500;600;700&family=DM+Sans:wght@400;500;600&display=swap" rel="stylesheet">
```

Meta: `<meta name="theme-color" content="#17342a">` (era `#1a4d2e`).

## Regras de composição (o que faz parecer o mockup)

1. **Header**: fundo `--brand-bg` sólido (nos dois temas), borda inferior `--brand-gold-line`. Título "O CÓDIGO DA LONGEVIDADE" em `--serif`, caixa alta, `letter-spacing:.14em`, cor `--brand-gold`, 14–15px, peso 700. Linha secundária em `--sans` 11px, `rgba(240,232,210,.68)`. Selo circular de 34px à esquerda (borda `--brand-gold-line`, ícone "broto" em SVG dourado — copiar o `.brand-mark` de qualquer módulo).
2. **Bottom-nav**: fundo `--brand-bg`, borda superior `--brand-gold-line`. Ícones SVG outline (stroke `currentColor`, 21px) — nada de emoji. Inativo `rgba(226,216,190,.55)`, ativo `--brand-gold-strong`. Os 4 SVGs (Início/Conteúdos/Progresso/Perfil) estão no rodapé de qualquer módulo deste repo — copiar de lá.
3. **Títulos** (h1/h2 e títulos de card): `--serif`, peso 700, cor `--heading`.
4. **Labels de seção** (ex. "BIBLIOTECA DE CONTEÚDOS"): `--sans` 11–12px, caixa alta, `letter-spacing:.09em`, peso 700, cor `--text-soft`; link "Ver todos" à direita em `--accent`.
5. **Aba Início — 3 blocos do mockup** (aplicar quando mexer no dashboard):
   - Linha de 4 categorias (Alimentação / Energia / Equilíbrio / Vitalidade) em cards quadrados `--bg-elevated` com borda `--border`, ícone outline dourado (`--accent`), rótulo 12px embaixo. Cada card linka pro(s) módulo(s) do tema.
   - Card "Continue de onde parou" com imagem (mesmas fotos Unsplash usadas nos módulos), título em `--serif`, botão pill `--brand-bg` com texto `--brand-gold-strong` em caps espaçadas ("COMECE POR AQUI →").
   - Cards de módulo com foto no topo, título `--serif`, descrição 13px `--text-soft` e um traço dourado de 28px (`border-bottom:2px solid --brand-gold`) no rodapé do card.
6. **Botões primários**: fundo `--brand-bg`, texto `--brand-gold-strong`, borda-radius 30px. Secundários: borda `--green`, texto `--green` (como o "Marcar como concluído" dos módulos).

## Onde aplicar na VPS (próxima sessão com SSH)

- `server.js` → HTML inline das rotas `/biblioteca` e `/entrar` (baixar via `scp`, editar, `node -c`, subir, `systemctl restart biblioteca-app`).
- Templates de e-mail em `/opt/biblioteca-app/templates/` — opcional, mas o dourado `#cfa963` + verde `#17342a` alinham o e-mail com o app.
- Os módulos deste repo precisam ser copiados pra `/var/www/valdoirmiranda-private/` (e `es/`, `en/`) após o `git pull`, como sempre.
