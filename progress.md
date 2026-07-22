# Biblioteca Valdoir Miranda | Estudos Avançados — Progresso

_Atualizado em 21/07/2026_

## Status geral

Produto **publicado na Hotmart com vendas ativas** (21/07/2026, autorizado pelo Ezequiel). Checkout: `https://pay.hotmart.com/V106821157P` · Página de vendas Hotmart: `https://go.hotmart.com/V106821157P`. Site com botões de compra ativos apontando pro checkout.

- Produto: "Biblioteca Valdoir Miranda | Estudos Avançados"
- ID Hotmart: 8164684
- Área de membros: Hotmart Club dedicado, slug `biblioteca-valdoir-miranda` (isolado de outros produtos seus, como o "Do Zero ao Profissional")
- Domínio próprio: **valdoirmiranda.com** (registrado na Porkbun, já configurado — ver seção Infraestrutura)

## Módulos

5 módulos criados, cada um com 1 aula publicada. Cada aula tem um texto de introdução + um link que abre a página de estudo interativa.

| Módulo | Arquivo |
|---|---|
| 1. Combinação de Alimentos | `b455ba4f3f.html` |
| 2. Alimentação e Energia | `f25ef86eb7.html` |
| 3. Vitalidade Masculina | `d786c82234.html` |
| 4. Corpo, Mente e Hábitos | `7d40d1ef04.html` |
| 5. Longevidade e Qualidade de Vida | `2adee283ae.html` |

## Infraestrutura (migrado do GitHub Pages para VPS própria)

- **VPS**: DigitalOcean, droplet `biblioteca-valdoir-vps` (Ubuntu 24.04, 512MB RAM + 1GB swap), IP `161.35.110.78`, US$ 4/mês
- **Domínio**: `valdoirmiranda.com` e `www.valdoirmiranda.com` apontando pro droplet via DNS (Porkbun), com HTTPS (Let's Encrypt, renovação automática configurada)
- **Site estático** (`index.html`, página de vendas/institucional): servido direto pelo nginx a partir do repositório `dev-zeq/valdoirmiranda` clonado em `/var/www/valdoirmiranda`
- **Os 5 módulos** ficaram fora da pasta pública (`/var/www/valdoirmiranda-private`) e só são liberados através do fluxo de login abaixo — não são mais acessíveis via link direto (nem os nomes aleatórios funcionam mais sozinhos)
- O antigo GitHub Pages não é mais a fonte servida ao público; o repositório GitHub continua sendo a fonte de verdade do código, mas quem serve ao vivo é a VPS

## Controle de acesso (implementado)

Backend Node.js (`/opt/biblioteca-app`, rodando como serviço systemd `biblioteca-app`, reinicia sozinho se cair):

- **Webhook da Hotmart** (`/webhook/hotmart`) cadastrado e testado (200 OK) — compra aprovada libera acesso automaticamente; cancelamento, reembolso ou chargeback revogam automaticamente
- **Login por e-mail** (`/entrar`): comprador digita o e-mail usado na compra, recebe um link de acesso válido por 24h
- **Biblioteca protegida** (`/biblioteca` → `/modulos/...`): só abre com sessão válida (cookie assinado), checando se o e-mail está com status "ativo"
- Dados de compradores/tokens guardados em `/opt/biblioteca-app/data.json` (arquivo simples, sem necessidade de banco de dados pro volume esperado)

## E-mail transacional — funcionando ✅

- Tentamos primeiro via Mailcow próprio (`mail.bezclean.com.br`) usando SMTP, mas o droplet da DigitalOcean bloqueia portas SMTP de saída (25/465/587) por padrão, política antispam deles — confirmado com teste direto contra o Gmail, que falhou igual. Abri o **ticket #12601558** na DigitalOcean pedindo a liberação (ainda em aberto, mas não é mais bloqueante).
- **Solução adotada**: Resend (envio via API HTTPS, não usa portas SMTP, então não esbarra no bloqueio). Domínio `valdoirmiranda.com` verificado na Resend (DKIM, MX e SPF no subdomínio `send.valdoirmiranda.com`, sem conflitar com o Mailcow no domínio raiz).
- Testado de ponta a ponta: compra aprovada (via webhook) → login em `/entrar` → e-mail chega de verdade com o link de acesso. **Confirmado recebido.**
- O domínio no Mailcow continua configurado e pode ser usado no futuro (ex: quando o ticket da DigitalOcean for resolvido, ou pra caixas de e-mail comuns tipo suporte@).

## Pendências

- ~~Templates de e-mail em HTML~~ — **feito**: e-mail de acesso agora usa template com a identidade visual do site (verde/âmbar, tipografia serifada no título), compatível com os principais clientes de e-mail (arquivo em `/opt/biblioteca-app/templates/email-access.html` na VPS). Testado e confirmado recebido corretamente.
- ~~Atualizar os links das aulas na Hotmart Club~~ — **feito**: as 5 aulas agora apontam para `https://valdoirmiranda.com/entrar` (fluxo novo de login) em vez do link antigo do GitHub Pages
- ~~Definir preço final de venda~~ — **feito**: R$ 37 (preço base na Hotmart, oferta `49b52jzx`), reembolso 7 dias
- ~~Decidir sobre publicar/ativar o produto pra venda~~ — **feito**: cadastro finalizado e vendas ativas em 21/07/2026
- Revisar a página de vendas do produto na Hotmart (gerada automaticamente, ainda não editada)
- Adicionar imagem de capa do produto na Hotmart (está sem imagem — placeholder cinza)
- Testar uma compra real de ponta a ponta (checkout → webhook → e-mail de acesso)
- Avaliar tradução do site pra outros idiomas (mencionado, não iniciado)
- (Opcional, não bloqueante) Acompanhar resposta do ticket #12601558 da DigitalOcean, caso queira usar SMTP do Mailcow no futuro

## Onde as coisas estão

- Repositório GitHub: `dev-zeq/valdoirmiranda` (index.html do site + os 5 arquivos de módulo, histórico de commits)
- VPS: DigitalOcean, droplet `biblioteca-valdoir-vps`, IP `161.35.110.78` (chave SSH em `~/.ssh/digitalocean_biblioteca_valdoir`)
- Domínio: Porkbun (`valdoirmiranda.com`), DNS gerenciado lá
- E-mail (envio): Resend, domínio `valdoirmiranda.com` verificado, API key configurada como variável de ambiente no serviço systemd da VPS
- E-mail (Mailcow, backup/futuro): `mail.bezclean.com.br` (painel próprio, domínio `valdoirmiranda.com` adicionado, caixa `acesso@valdoirmiranda.com` criada)
- Painel Hotmart: produto 8164684, dentro do Club "biblioteca-valdoir-miranda", webhook cadastrado em Ferramentas → Webhook
