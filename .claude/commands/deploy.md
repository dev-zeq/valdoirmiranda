---
description: Faz o deploy do repositório valdoirmiranda pra VPS de produção (git pull + sincroniza os módulos privados)
---

Você está rodando localmente, com acesso SSH real à VPS de produção. Siga esses passos, nessa ordem, e narre o que for fazendo:

## 1. Garantir que o repositório local está atualizado
- `git status` (checar se não há mudanças locais não commitadas — se houver, avisar e parar, não sobrescrever nada)
- `git checkout main && git pull origin main`

## 2. Conferir se há PR aberto ainda não mergeado
- Se o usuário mencionou um PR específico (ex: "#3"), perguntar se já foi mergeado antes de continuar. Se não foi, mergear primeiro (ou pedir confirmação) antes do deploy.

## 3. Deploy do site institucional + módulos (público)
- SSH na VPS: `ssh -i ~/.ssh/digitalocean_biblioteca_valdoir root@161.35.110.78` (ajustar usuário se não for root)
- Dentro da VPS: `cd /var/www/valdoirmiranda && git pull`
- Guardar a lista de arquivos que o `git pull` alterou (aparece no output do pull, ou rode `git diff --stat HEAD@{1} HEAD`)

## 4. Sincronizar módulos privados (se necessário)
- Os módulos ficam também em `/var/www/valdoirmiranda-private/` (fora da pasta pública, só acessível pelo login) — cópias manuais, não symlink; cada módulo existe em 3 versões: raiz (PT), `es/` e `en/`
- Depois do `git pull` do passo 3, rodar o script de sincronização — ele deriva o destino do caminho de origem (cobre raiz, `es/` e `en/` sozinho):
  `/var/www/valdoirmiranda/infra/sync-private.sh`
- O script lista o que copiou e quantos arquivos ignorou (sem espelho privado). Confirmar que os módulos apareceram como "copiado".
- Atenção: o script só sincroniza arquivos que **já têm** espelho privado. Se um módulo novo entrar no repo, copiá-lo à mão uma vez pra pasta privada (raiz, `es/`, `en/`) antes de o script passar a segui-lo.

## 5. O que este comando NÃO faz (e por quê)
- **Não mexe no `server.js` nem nos templates de e-mail** — esses arquivos vivem só na VPS (`/opt/biblioteca-app`), não fazem parte deste repositório git. Se alguma tarefa pedir mudança neles, isso é um processo separado: baixar com `scp`, editar, `node -c server.js` pra validar sintaxe, subir de volta, e só então `systemctl restart biblioteca-app`. Nunca reiniciar o serviço sem validar a sintaxe antes.
- **Não mexe no nginx** — se uma rota nova foi adicionada no `server.js`, isso precisa ser adicionado manualmente em `/etc/nginx/sites-available/valdoirmiranda` (cópia de referência em `infra/nginx-valdoirmiranda.conf` neste repo), testado com `nginx -t` e recarregado com `systemctl reload nginx`. Avisar o usuário se notar que isso pode ser necessário, mas não fazer automaticamente.

## 6. Confirmar no final
- Reportar exatamente quais arquivos foram atualizados na VPS (público e/ou privado)
- Se algo no passo 5 parecer necessário (mudança de backend/nginx pendente), avisar explicitamente em vez de tentar resolver sozinho
