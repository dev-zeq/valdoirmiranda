# O Código da Longevidade — Progresso

_Atualizado em 23/07/2026_

## Status geral

Produto **publicado na Hotmart com vendas ativas**, site no ar, backend de acesso funcionando de ponta a ponta (compra → e-mail → login → módulos). Praticamente pronto pra vender de verdade — falta só revisar a página de vendas automática da Hotmart e decidir sobre a capa do produto lá.

- **Nome do produto**: "O Código da Longevidade | por Valdoir Miranda" (renomeado de "Biblioteca Valdoir Miranda" em 21/07/2026 — posicionamento de longevidade pra todos os públicos, não só masculino)
- **ID Hotmart**: 8164684
- **Preço**: R$ 37 (preço de fundador, sobe pra R$ 67 quando o acervo chegar a 100%), pagamento único, reembolso 7 dias
- **Checkout**: `https://pay.hotmart.com/V106821157P` · Página de vendas: `https://go.hotmart.com/V106821157P`
- **Categoria**: vendido como "curso" (Cursos Online / Área de Membros na Hotmart) — decisão consciente: não é ebook (tem progresso salvo, "marcar como concluído", interatividade) nem curso em vídeo (não tem vídeo-aula nenhuma). Conferido: nenhum texto do site promete vídeo, então "curso" não gera expectativa quebrada.
- **Domínio**: `valdoirmiranda.com` (Porkbun)
- **Área de membros**: Hotmart Club, slug `biblioteca-valdoir-miranda`

## Módulos (conteúdo pago)

6 módulos, cada um uma página HTML interativa (índice lateral, progresso salvo por seção, sanfonas, comparações clicáveis):

| Módulo | Arquivo |
|---|---|
| 1. Combinação de Alimentos | `b455ba4f3f.html` |
| 2. Alimentação e Energia (+ seção 06 "Guia rápido de alimentos", adicionada 22/07) | `f25ef86eb7.html` |
| 3. Vitalidade Masculina | `d786c82234.html` |
| 4. Corpo, Mente e Hábitos | `7d40d1ef04.html` |
| 5. Longevidade e Qualidade de Vida | `2adee283ae.html` |
| 6. Vitalidade Feminina (novo, 23/07) | `c16240ae3d.html` |

**Vitalidade Feminina (23/07/2026):** a Bruna notou que só existia módulo de vitalidade pro público masculino. Diferente dos outros módulos (que vêm de material próprio do Valdoir), esse foi construído do zero via pesquisa (WebSearch), com grade de evidência forte/moderada/fraca — ver [[feedback_evidence_graded_content]]. Espelha as mesmas 5 seções do módulo masculino (hormônios/ciclo, sono, treino de força e densidade óssea, alimentação, estresse crônico). **Importante:** por não vir de observação pessoal do Valdoir sobre esse tema específico, o módulo NÃO tem o bloco "✒️ Observação do Autor" que os outros módulos usam — evita atribuir a ele uma autoridade pessoal que não existe nessa área. Já traduzido pra ES/EN (`es/c16240ae3d.html`, `en/c16240ae3d.html`). Ordem corrigida a pedido do Ezequiel: fica logo depois de Vitalidade Masculina (dashboard e página de vendas), não mais por último.

## Cabeçalho dos módulos (23/07/2026)

- Botão "🏠" adicionado ao lado do botão de tema nos 6 módulos, linkando pra `/biblioteca` — resolvia a falta de navegação de volta no celular (só dava pra usar o botão "voltar" do navegador).
- Título do cabeçalho reformulado: linha principal virou "O Código da Longevidade" (era "Valdoir Miranda | Estudos Avançados", que ficava cortado no mobile sem reticências por causa de `text-overflow` não funcionar direito num flexbox); autor + nome do módulo desceram pra linha pequena.

## Página de vendas — ajustes de copy (23/07/2026)

- **Hero reformulado**: título principal virou "O Código da Longevidade" (era o nome "Valdoir Barreto Miranda") — Valdoir ainda é desconhecido pro público frio, então o produto vira o destaque visual e ele aparece como autor no parágrafo de apoio ("reunidas por Valdoir Miranda — pesquisador independente —"). A seção "Quem é Valdoir" mais abaixo continua intacta com a biografia completa.
- **"+50 materiais" removido** de todos os 3 lugares onde aparecia (chip flutuante, estatística, texto do acervo) — dava a entender que o produto teria 50 módulos, quando na real o material bruto do Valdoir é organizado e distribuído dentro dos módulos existentes. Trocado por "Décadas de estudo".
- **3 selos de destaque** adicionados na seção do acervo: 📱 Funciona liso no celular / 🎨 Visual moderno e intuitivo / ✅ Progresso salvo automaticamente.
- **Barra "Organização do acervo"**: atualizada de 35% pra 60% (avanço real na organização, confirmado com o Ezequiel antes de mudar — não é só ajuste de marketing).
- **Card da Vitalidade Feminina** também adicionado na seção "Áreas de Pesquisa" (mais genérica, sobre temas de estudo) — só tinha o card de Vitalidade Masculina lá, mesma inconsistência da seção de módulos.
- Tudo sincronizado nos 3 idiomas via `build_i18n.py` (tabela de tradução atualizada junto com cada mudança).

**Guia rápido de alimentos (22/07/2026):** o pai do Ezequiel (Valdoir) mandou um álbum do Google Fotos ("FISH 100%", ~29 slides) com conteúdo sobre benefícios de alimentos, num template visual carregado (fundo verde neon, marca "Medicina Integrativa" sem relação com o produto). Revisei ~13 dos 29 slides e reescrevi 9 alimentos + 1 hábito em tom naturalista/observacional (não clínico), removendo:
- Um mito sem comprovação científica (cebola cortada "absorve toxina do ar")
- Promoção de marca de terceiro (produto "Pólen Baldoni") com alegações médicas fortes ("cura próstata", "efeito antibiótico") — mantive o tema pólen apícola, só tirei a marca e as alegações
- Erros de português (ex.: "as sementes de chia tem" → "têm")

**Pendente:** ~14-16 slides do álbum ainda não foram abertos/revisados. Se quiser completar, o método que funcionou foi: abrir o álbum compartilhado no Google Fotos, clicar em cada foto, e capturar a URL da imagem através da resposta da API interna (`rpcids=VrseUb` nas requisições de rede) — as miniaturas comprimidas não são legíveis. Também ficou pendente confirmar com o Valdoir se a regra "não misturar tubérculos na mesma refeição" (slide de tubérculos/raízes) é intencional (linha da trofologia/combinação de alimentos, não é consenso científico mainstream, mas pode ser proposital dado que o Módulo 1 é sobre isso).

## Módulos multilíngues (23/07/2026)

Pedido do Ezequiel — amigos vão vender o produto no Peru e países vizinhos, então os 5 módulos pagos agora existem em 3 idiomas, não só o site institucional:

- **Arquivos**: `es/` e `en/` na raiz do repo (mesmos 5 nomes-hash, conteúdo traduzido), espelhando a estrutura do site institucional. Na VPS ficam em `/var/www/valdoirmiranda-private/es/` e `/en/` (pastas novas, criadas nesse dia).
- **Preferência de idioma por comprador**: campo `language` (`pt`/`es`/`en`, padrão `pt`) salvo no `data.json` de cada comprador. Duas formas de setar:
  1. Link de origem: `/entrar?lang=es` (útil pra linkar direto da futura página de vendas em espanhol dos amigos) — grava a preferência assim que a pessoa faz login pela primeira vez.
  2. Seletor manual dentro do `/biblioteca` (PT / ES / EN, rota `/idioma/:lang`) — só aparece na entrada principal, não dentro de cada módulo.
- **Tudo localizado**: página de login, dashboard `/biblioteca`, e-mail de acesso (`templates/email-access.{pt,es,en}.html`) e o conteúdo dos 5 módulos. `/modulos/:file` decide sozinho (no `server.js`) de qual pasta servir, com fallback pro português se um arquivo traduzido não existir.
- **nginx**: precisou adicionar `location /idioma/ { proxy_pass ... }` (rota nova, mesma pegadinha do `/sair` antes — allowlist explícita).
- **Tradução**: feita por agentes em paralelo, preservando 100% da estrutura HTML/CSS/JS e traduzindo só o texto visível; vocabulário adaptado pro espanhol latino-americano onde fazia sentido (palta, camote, quinua, frijoles).
- **Testado ponta a ponta**: login, e-mail, dashboard e conteúdo dos módulos nos 3 idiomas, incluindo troca de idioma pelo seletor.
- **Nomenclatura do produto por idioma** (já usada no site institucional, reaproveitada no backend): PT "O Código da Longevidade", ES "El Código de la Longevidad", EN "The Longevity Code".

## Site institucional (trilíngue)

3 idiomas com URLs próprias e seletor no menu:
- Português (padrão): `valdoirmiranda.com/` → `index.html`
- Espanhol: `valdoirmiranda.com/es/` → `es/index.html`
- Inglês: `valdoirmiranda.com/en/` → `en/index.html`

Tags `hreflang` no `<head>` de todas pro Google indexar a versão certa por país. As páginas EN/ES são geradas a partir da PT pelo script `build_i18n.py` (raiz do repo, tabela de tradução PT→EN→ES) — **ao editar textos, altere o `index.html`, rode `python3 build_i18n.py` e comite os 3 arquivos** pra não dessincronizar. Preço mantido em R$ nas 3 versões (nota "convertido pra sua moeda no checkout" — a Hotmart converte automático).

## Infraestrutura

- **VPS**: DigitalOcean, droplet `biblioteca-valdoir-vps` (Ubuntu 24.04, 512MB RAM + 1GB swap), IP `161.35.110.78`, US$ 4/mês. SSH: `~/.ssh/digitalocean_biblioteca_valdoir`
- **Site institucional** (`index.html` + `/es/` + `/en/`): nginx serve direto de `/var/www/valdoirmiranda` (clone do repo `dev-zeq/valdoirmiranda`)
- **Os 5 módulos**: ficam em `/var/www/valdoirmiranda-private` (fora da pasta pública), só acessíveis pelo fluxo de login — **precisam ser copiados manualmente pra lá depois de cada `git pull`** (não é sincronizado automaticamente, ver seção "Como fazer deploy")
- **nginx**: config em `/etc/nginx/sites-available/valdoirmiranda`, cópia salva em `infra/nginx-valdoirmiranda.conf` no repo. Só repassa pro backend Node as rotas explícitas: `/webhook/`, `/entrar`, `/biblioteca`, `/sair`, `/modulos/`. Qualquer rota nova no `server.js` **precisa ser adicionada aqui também**, senão dá 404 (aconteceu com `/sair`, já corrigido)
- **HTTPS**: Let's Encrypt, renovação automática

## Backend de acesso (`server.js`)

Node.js em `/opt/biblioteca-app`, roda como serviço systemd `biblioteca-app` (reinicia sozinho se cair). **O `server.js` e os templates vivem só na VPS, não no repositório git** — sempre baixar (`scp`), editar localmente, testar sintaxe (`node -c`) e subir de volta antes de reiniciar o serviço.

- **Webhook Hotmart** (`/webhook/hotmart`): compra aprovada libera acesso automaticamente; cancelamento/reembolso/chargeback revogam automaticamente. Testado (200 OK).
- **Login por e-mail** (`/entrar`): compra digita e-mail, recebe link válido por 24h.
- **Sessão salva: 90 dias** (era 24h, aumentado 22/07 a pedido do Ezequiel — o link do e-mail continua expirando em 24h, só o cookie de sessão pós-clique dura mais). Reembolso revoga o acesso na hora mesmo com sessão de 90 dias, porque a checagem roda a cada página, não fica em cache no cookie.
- **Dashboard `/biblioteca`**: redesenhado 22/07 (era uma lista de links azuis sem estilo) — agora cards com ícone/título/descrição de cada módulo, no mesmo visual dos módulos internos. Tem botão "Sair" (`/sair`, novo).
- **Dados de compradores**: `/opt/biblioteca-app/data.json` (arquivo simples). Estrutura: `{"purchasers": {"email": {"status": "active"|"revoked", ...}}, "tokens": {...}}`.
- **Acesso do dono**: `zeqmiranda@gmail.com` foi marcado manualmente como `status: 'active'` (`transaction_id: 'manual-owner-access'`) direto no `data.json` — acesso vitalício sem passar pela Hotmart, útil pra sempre poder conferir o produto como comprador real vê.

## App instalável (PWA)

Site instalável como app no celular ("Adicionar à tela de início"), sem loja de app:
- Ícone próprio (folha estilizada verde/âmbar) em `icons/`, `manifest.json` na raiz
- `sw.js` (service worker): módulos e `/biblioteca` já visitados ficam salvos no aparelho, abrem offline (estratégia "tenta rede, cai pro cache se falhar")
- Tags de manifest/ícone precisam estar nos 5 módulos **e** nas páginas `/entrar` e `/biblioteca` do `server.js` — se reeditar o backend, manter esses blocos
- Testado: manifest, ícones e sw.js servem certo (200), service worker registra e ativa, cache confirmado guardando página visitada

## E-mail transacional — funcionando ✅

- **Envio**: Resend (API HTTPS, não usa porta SMTP). Domínio `valdoirmiranda.com` verificado (DKIM/MX/SPF em `send.valdoirmiranda.com`).
- Testado ponta a ponta: compra → `/entrar` → e-mail chega com link de acesso. Template com identidade visual do site em `/opt/biblioteca-app/templates/email-access.html` (na VPS, não no repo).
- **SMTP direto (Mailcow) bloqueado pela DigitalOcean** — ticket #12601558 negado em 21/07/2026. Não é bloqueante (Resend resolve tudo), mas se quiser usar o Mailcow (`mail.bezclean.com.br`, caixa `acesso@valdoirmiranda.com` já criada) no futuro, precisa de porta alternativa (2525) ou relay via API.

## Programa de afiliados

- **Comissão: 50%** por venda aprovada — mas atenção: é 50% do valor líquido (após taxa da Hotmart), não dos R$ 37 cheios. Na prática dá **~R$ 16,17 por venda**, não R$ 18,50. Já corrigido em todo lugar (texto na Hotmart, página de afiliados).
- **Página de recrutamento de afiliados**: `afiliados.valdoirmiranda.com` — repositório **separado** no GitHub (`dev-zeq/valdoirmiranda-afiliados`), com GitHub Pages próprio (domínio customizado, HTTPS via Let's Encrypt do próprio GitHub). **Não faz parte do repo `dev-zeq/valdoirmiranda`** — pra atualizar essa página, editar `afiliados.html` localmente e fazer push pro outro repo (não pro principal).
- Link direto de afiliação: `https://affiliate.hotmart.com/affiliate-recruiting/view/3159O106821178`
- **Pendência conhecida, não crítica**: a página pública de recrutamento na própria Hotmart mostra o texto de divulgação **duplicado** (uma cópia certa com R$16,17, uma cópia antiga com R$18,50). Só achei um campo editável nas configurações (já corrigido); a duplicação pode ser um comportamento de cache do lado da Hotmart. Se persistir depois de alguns dias, vale abrir chamado com o suporte deles.

## Como fazer deploy (checklist rápido)

1. **Site institucional / módulos (arquivos HTML)**: editar local → `git commit` + `git push` → `ssh` na VPS → `git pull` em `/var/www/valdoirmiranda` → se mudou algum dos 5 módulos, copiar manualmente pra `/var/www/valdoirmiranda-private/`
2. **Backend (`server.js`, templates de e-mail)**: baixar da VPS com `scp` → editar local → `node -c server.js` (checar sintaxe) → `scp` de volta → `systemctl restart biblioteca-app` na VPS
3. **nginx**: se adicionar rota nova no `server.js`, adicionar também em `/etc/nginx/sites-available/valdoirmiranda` → `nginx -t` (testar) → `systemctl reload nginx`. Sempre fazer backup do arquivo antes (`cp arquivo arquivo.bak`).
4. **Página de afiliados**: repo separado `dev-zeq/valdoirmiranda-afiliados`, GitHub Pages atualiza sozinho após o push.

## Pendências

- Revisar a página de vendas do produto na Hotmart (gerada automaticamente pela Hotmart, ainda não editada manualmente)
- Adicionar imagem de capa do produto na Hotmart (tenho uma pronta: `capa-hotmart.png` na raiz do repo — falta só fazer o upload manual no painel, é um passo que exige interação de arquivo do sistema)
- Testar uma compra real de ponta a ponta (checkout pago de verdade → webhook → e-mail) — só testei o fluxo de login manualmente, nunca uma compra 100% real
- Confirmar com o Valdoir a regra dos tubérculos (não misturar tubérculos na mesma refeição, ver seção Módulos) — ainda não confirmado se é intencional
- Acompanhar se a duplicação de texto na página de afiliados da Hotmart se resolve sozinha (ver seção Afiliados)
- Avisar os amigos que vão vender no Peru que o backend já suporta ES/EN completo (login, e-mail, dashboard, os 6 módulos) — falta só eles terem a página de vendas deles em espanhol linkando pra `/entrar?lang=es`
- Revisar com calma o restante do conteúdo dos "piores alimentos" do álbum do Valdoir (açúcar, farinha, industrializados etc.) — só entrou o essencial dos 6 itens novos (alho, peixe, kefir, especiarias, magnésio, limão) e a nota sobre iodo/tireoide; a seção de "alimentos a evitar" tem bastante alegação exagerada/imprecisa (ex. "farinha integral pior que a branca", "glúten aumentou 400x") que ainda precisa da mesma triagem antes de virar conteúdo, se quiserem usar

## Onde as coisas estão

- **Repositório principal**: `dev-zeq/valdoirmiranda` — site institucional (PT/ES/EN), os 5 módulos, PWA (manifest/ícones/sw.js), config do nginx documentada em `infra/`
- **Repositório da página de afiliados**: `dev-zeq/valdoirmiranda-afiliados` (separado, GitHub Pages próprio)
- **VPS**: DigitalOcean, IP `161.35.110.78`, chave SSH `~/.ssh/digitalocean_biblioteca_valdoir`. Backend Node em `/opt/biblioteca-app` (fora do git), módulos privados em `/var/www/valdoirmiranda-private`, site público em `/var/www/valdoirmiranda`
- **Domínio**: Porkbun (`valdoirmiranda.com`), DNS gerenciado lá
- **E-mail (envio)**: Resend, domínio verificado, API key na VPS
- **E-mail (Mailcow, backup/futuro)**: `mail.bezclean.com.br`
- **Painel Hotmart**: produto 8164684, dentro do Club "biblioteca-valdoir-miranda"
