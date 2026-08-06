import os

def define_env(env):
    def _recuperar_todas_las_publicaciones():
        docs_dir = env.conf['docs_dir']
        publicaciones = []
        for root, dirs, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md') and file not in ['index.md', 'publicaciones.md']:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lineas = f.readlines()
                        if lineas and lineas[0].strip() == '---':
                            metadata = {}
                            i = 1
                            while i < len(lineas) and lineas[i].strip() != '---':
                                linea = lineas[i]
                                if ':' in linea:
                                    clave, valor = linea.split(':', 1)
                                    clave_limpia = clave.strip()
                                    valor_limpio = valor.strip().strip('"').strip("'")
                                    if clave_limpia == 'etiquetas':
                                        valores_internos = valor_limpio.strip('[]')
                                        metadata[clave_limpia] = [t.strip() for t in valores_internos.split(',') if t.strip()]
                                    else:
                                        metadata[clave_limpia] = valor_limpio
                                i += 1
                                
                            if 'titulo' in metadata and 'fecha' in metadata:
                                ruta_relativa = os.path.relpath(file_path, docs_dir).replace('\\', '/')
                                
                                metadata['archivo_md'] = ruta_relativa
                                
                                if ruta_relativa.endswith('.md'):
                                    metadata['url'] = ruta_relativa[:-3] + '/'
                                else:
                                    metadata['url'] = ruta_relativa
                                
                                metadata['directorio_padre'] = os.path.dirname(ruta_relativa)
                                
                                partes = metadata['fecha'].split('-')
                                if len(partes) == 3:
                                    metadata['fecha_bonita'] = f"{partes[2]}-{partes[1]}-{partes[0]}"
                                else:
                                    metadata['fecha_bonita'] = metadata['fecha']
                                    
                                if 'imagen' not in metadata:
                                    metadata['imagen'] = "pics/default-thumb.jpg"
                                    metadata['es_externa'] = False
                                else:
                                    metadata['es_externa'] = metadata['imagen'].startswith('http')
                                    
                                publicaciones.append(metadata)
                    except Exception:
                        pass
        return publicaciones

    todas_las_pubs = _recuperar_todas_las_publicaciones()
    todas_las_pubs.sort(key=lambda x: x['fecha'], reverse=True)
    
    if 'extra' not in env.conf:
        env.conf['extra'] = {}
    env.conf['extra']['publicaciones_sidebar'] = todas_las_pubs[:3]

    @env.macro
    def obtener_ultimas_publicaciones(limite=5):
        publicaciones = _recuperar_todas_las_publicaciones()
        publicaciones.sort(key=lambda x: x['fecha'], reverse=True)
        markdown_final = '<div class="lista-tarjetas">\n'
        for p in publicaciones[:limite]:
            imagen_url = p.get('imagen', 'pics/default-thumb.jpg')
            es_externa = imagen_url.startswith('http')
            ruta_imagen = imagen_url if es_externa else f"../{imagen_url}"
            descripcion = p.get('descripcion', 'Haz clic para leer la publicación completa...')
            
            markdown_final += f"""
            <div class="tarjeta-articulo">
                <div class="tarjeta-imagen">
                    <img src="{ruta_imagen}" alt="{p['titulo']}">
                </div>
                <div class="tarjeta-info">
                    <h3><a href="../{p['url']}">{p['titulo']}</a></h3>
                    <span class="tarjeta-meta">📅 {p.get('fecha_bonita', '')} — ✍🏻 {p.get('autor', 'Lulo')}</span>
                    <p class="tarjeta-descripcion">{descripcion}</p>
                </div>
            </div>
            """
        markdown_final += '</div>'
        return markdown_final

    @env.macro
    def obtener_navegacion_arbol():
        publicaciones = _recuperar_todas_las_publicaciones()
        arbol = {}
        for p in publicaciones:
            ruta_carpeta = p['directorio_padre']
            partes_ruta = ruta_carpeta.split('/') if ruta_carpeta else []
            nodo_actual = arbol
            for parte in partes_ruta:
                if parte not in nodo_actual:
                    nodo_actual[parte] = {'_archivos': [], '_subcarpetas': {}}
                nodo_actual = nodo_actual[parte]['_subcarpetas']
            if not ruta_carpeta:
                if '_raiz' not in arbol:
                    arbol['_raiz'] = {'_archivos': [], '_subcarpetas': {}}
                arbol['_raiz']['_archivos'].append(p)
            else:
                n = arbol
                for i, parte in enumerate(partes_ruta):
                    if i == len(partes_ruta) - 1:
                        if '_archivos' not in n[parte]:
                            n[parte]['_archivos'] = []
                        n[parte]['_archivos'].append(p)
                    else:
                        n = n[parte]['_subcarpetas']

        def renderizar_nodo(nodo, nombre_nodo, nivel=0):
            output = ""
            sangria = "    " * nivel
            nombre_bonito = nombre_nodo.replace('_', ' ').title()
            if nombre_nodo != '_raiz':
                output += f"{sangria}* **{nombre_bonito}**:\n"
                nivel_hijo = nivel + 1
                sangria_hijo = "    " * nivel_hijo
            else:
                nivel_hijo = nivel
                sangria_hijo = "    " * nivel_hijo

            subcarpetas = nodo.get('_subcarpetas', {})
            for sub in sorted(subcarpetas.keys()):
                output += renderizar_nodo(subcarpetas[sub], sub, nivel_hijo)

            articulos = nodo.get('_archivos', [])
            articulos.sort(key=lambda x: x['url'])
            for art in articulos:
                output += f"{sangria_hijo}* [{art['titulo']}]({art['archivo_md']}) por *{art.get('autor', 'Lulo')}*\n"
            return output

        markdown_final = ""
        for carpeta_principal in sorted([k for k in arbol.keys() if k != '_raiz']):
            markdown_final += renderizar_nodo(arbol[carpeta_principal], carpeta_principal, nivel=0)
        if '_raiz' in arbol:
            for art in arbol['_raiz'].get('_archivos', []):
                markdown_final += f"* [{art['titulo']}]({art['archivo_md']}) por *{art.get('autor', 'Lulo')}*\n"
        return markdown_final

    @env.macro
    def obtener_indice_seccion():
        page_src_path = env.page.file.src_path.replace('\\', '/')
        carpeta_actual = os.path.dirname(page_src_path)
        publicaciones = _recuperar_todas_las_publicaciones()
        articulos_locales = [p for p in publicaciones if p['directorio_padre'] == carpeta_actual]
        articulos_locales.sort(key=lambda x: x['url'])
        if not articulos_locales:
            return "_Próximamente se añadirán publicaciones a esta sección._\n"
        markdown_output = ""
        for art in articulos_locales:
            nombre_archivo = os.path.basename(art['archivo_md'])
            markdown_output += f"* [{art['titulo']}]({nombre_archivo}) por *{art.get('autor', 'Lulo')}*\n"
        return markdown_output

    @env.macro
    def generar_buscador_etiquetas():
        publicaciones = _recuperar_todas_las_publicaciones()
        
        set_etiquetas = set()
        for p in publicaciones:
            for tag in p.get('etiquetas', []):
                set_etiquetas.add(tag)
        lista_etiquetas = sorted(list(set_etiquetas))
        
        html = '<div class="filtro-etiquetas-layout" style="margin-bottom: 25px; display: flex; flex-wrap: wrap; gap: 8px;">'
        html += '<button class="btn-tag-filtro" data-target="todos" style="padding: 6px 14px; border: 1px solid #3b82f6; background-color: #3b82f6; color: white; border-radius: 20px; cursor: pointer; font-family: inherit; font-size: 0.9em; transition: all 0.2s;">Todos</button>'
        for tag in lista_etiquetas:
            html += f'<button class="btn-tag-filtro" data-target="{tag}" style="padding: 6px 14px; border: 1px solid #e2e8f0; background-color: #f8fafc; color: #1e293b; border-radius: 20px; cursor: pointer; font-family: inherit; font-size: 0.9em; transition: all 0.2s;">#{tag}</button>'
        html += '</div>'
        
        html += '<div class="lista-articulos-filtrables" style="display: flex; flex-direction: column; gap: 16px;">'
        for p in publicaciones:
            tags_del_articulo = ",".join(p.get('etiquetas', []))
            
            pildoras_html = ""
            for tag in p.get('etiquetas', []):
                pildoras_html += f'<span style="background-color: #e2e8f0; padding: 2px 8px; border-radius: 12px; font-size: 0.8em; margin-right: 6px; color: #1e293b; font-weight: 500;">#{tag}</span>'
            
            html += f"""
            <div class="tarjeta-filtrable" data-tags="{tags_del_articulo}" style="padding: 16px; border: 1px solid #e2e8f0; border-radius: 8px; background-color: white; transition: transform 0.2s; box-shadow: 0 1px 3px rgba(0,0,0,0.05);">
                <h3 style="margin: 0 0 6px 0;"><a href="{env.conf.get('site_url', '')}{env.conf.get('base_url', '')}/{p['url']}" style="color: #1e3a8a; text-decoration: none; font-weight: 600;">{p['titulo']}</a></h3>
                <div style="font-size: 0.85em; color: #64748b; margin-bottom: 8px;">📅 {p.get('fecha_bonita', '')} — ✍🏻 {p.get('autor', 'Lulo')}</div>
                <div style="margin-top: 6px;">{pildoras_html}</div>
            </div>
            """
        html += '</div>'
        
        html += "<script>document.addEventListener('DOMContentLoaded',function(){const btns=document.querySelectorAll('.btn-tag-filtro'),cards=document.querySelectorAll('.tarjeta-filtrable');btns.forEach(b=>{b.addEventListener('click',function(){btns.forEach(x=>{x.style.backgroundColor='#f8fafc';x.style.color='#1e293b';x.style.borderColor='#e2e8f0'});this.style.backgroundColor='#3b82f6';this.style.color='white';this.style.borderColor='#3b82f6';const t=this.getAttribute('data-target');cards.forEach(c=>{if(t==='todos'){c.style.display='block'}else{const s=c.getAttribute('data-tags').split(',');if(s.includes(t)){c.style.display='block'}else{c.style.display='none'}}})})})});</script>"
        
        return html

    @env.macro
    def mostrar_etiquetas():
        etiquetas = env.page.meta.get('etiquetas', [])
        if not etiquetas:
            return ""
        
        html = '<div style="margin-top: 10px; display: flex; gap: 8px; flex-wrap: wrap;">'
        for tag in etiquetas:
            html += f'<span class="btn-tag-filtro" style="padding: 4px 10px; background-color: #e2e8f0; color: #1e293b; border-radius: 6px; font-size: 0.85rem; border: 1px solid #cbd5e1;">{tag}</span>'
        html += '</div>'
        return html
        
    def _generar_destacadas():
        docs_dir = env.conf['docs_dir']
        destacadas = []
        
        for root, dirs, files in os.walk(docs_dir):
            for file in files:
                if file.endswith('.md') and file not in ['index.md', 'publicaciones.md']:
                    file_path = os.path.join(root, file)
                    try:
                        with open(file_path, 'r', encoding='utf-8') as f:
                            lineas = f.readlines()
                        
                        if lineas and lineas[0].strip() == '---':
                            metadata = {}
                            i = 1
                            while i < len(lineas) and lineas[i].strip() != '---':
                                linea = lineas[i]
                                if ':' in linea:
                                    clave, valor = linea.split(':', 1)
                                    metadata[clave.strip().lower()] = valor.strip().strip('"').strip("'")
                                i += 1
                            
                            es_destacado = metadata.get('destacado') == 'true' or metadata.get('destacada') == 'true'
                            
                            if es_destacado:
                                rel_path = os.path.relpath(file_path, docs_dir).replace('\\', '/')
                                url = rel_path.replace('.md', '/')
                                
                                destacadas.append({
                                    'titulo': metadata.get('titulo', file[:-3]),
                                    'url': url,
                                    'imagen': metadata.get('imagen', 'pics/mini_elect.jpg'),
                                    'nivel': metadata.get('nivel', 'Fácil'),
                                    'tiempo': metadata.get('tiempo', '10 min'),
                                    'fecha_bonita': metadata.get('fecha', ''),
                                    'autor': metadata.get('autor', 'Lulo'),
                                    'descripcion': metadata.get('descripcion', 'Haz clic para leer esta publicación destacada...')
                                })
                    except Exception as e:
                        print(f"Error al leer el archivo {file}: {e}")
                        
        try:
            destacadas.sort(key=lambda x: x['fecha_bonita'], reverse=True)
        except:
            pass
            
        return destacadas

    env.conf['extra']['publicaciones_destacadas'] = _generar_destacadas()
