{\rtf1\ansi\ansicpg1252\cocoartf2868
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fnil\fcharset0 Menlo-Regular;}
{\colortbl;\red255\green255\blue255;\red111\green14\blue195;\red236\green241\blue247;\red0\green0\blue0;
\red77\green80\blue85;\red24\green112\blue43;\red164\green69\blue11;}
{\*\expandedcolortbl;;\cssrgb\c51765\c18824\c80784;\cssrgb\c94118\c95686\c97647;\cssrgb\c0\c0\c0;
\cssrgb\c37255\c38824\c40784;\cssrgb\c9412\c50196\c21961;\cssrgb\c70980\c34902\c3137;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs28 \cf2 \cb3 \expnd0\expndtw0\kerning0
\outl0\strokewidth0 \strokec2 import\cf0 \strokec4  streamlit \cf2 \strokec2 as\cf0 \strokec4  st\cb1 \
\cf2 \cb3 \strokec2 from\cf0 \strokec4  datetime \cf2 \strokec2 import\cf0 \strokec4  datetime, date\cb1 \
\cf2 \cb3 \strokec2 import\cf0 \strokec4  pandas \cf2 \strokec2 as\cf0 \strokec4  pd\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # CONFIGURACI\'d3N DE LA P\'c1GINA\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.set_page_config(\cb1 \
\cb3     page_title=\cf6 \strokec6 "Prog. Operativo Cirug\'eda General"\cf0 \strokec4 ,\cb1 \
\cb3     page_icon=\cf6 \strokec6 "\uc0\u9877 \u65039 "\cf0 \strokec4 ,\cb1 \
\cb3     layout=\cf6 \strokec6 "wide"\cf0 \strokec4 ,\cb1 \
\cb3     initial_sidebar_state=\cf6 \strokec6 "expanded"\cf0 \cb1 \strokec4 \
\cb3 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # BASE DE DATOS SIMULADA (Extra\'edda del PDF)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # Diccionario principal de residentes con sus datos\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 RESIDENTES = \{\cb1 \
\cb3     \cf5 \strokec5 # R4\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 "Beltr\'e1n Delgado Jorge Omar"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R4"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Estado nutricional en pacientes ingresados para cirug\'eda de urgencia en Hospital Civil de Culiac\'e1n"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-10-05"\cf0 \strokec4 , \cf6 \strokec6 "2026-10-16"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-01-18"\cf0 \strokec4 , \cf6 \strokec6 "2027-01-29"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 3\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 4\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 5\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 6\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 8\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Pedi\'e1trica (HPS)"\cf0 \strokec4 , \cf7 \strokec7 9\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Pedi\'e1trica (HPS)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Soto Valle Jos\'e9 Ema\'fas"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R4"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Correlaci\'f3n entre aspectos cl\'ednicos y prote\'edna C reactiva como marcadores para fuga anastom\'f3tica intestinal"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-11-30"\cf0 \strokec4 , \cf6 \strokec6 "2026-12-11"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-05-04"\cf0 \strokec4 , \cf6 \strokec6 "2026-05-15"\cf0 \strokec4 )], \cf5 \strokec5 # Ajuste de a\'f1o l\'f3gico seg\'fan PDF\cf0 \cb1 \strokec4 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 5\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (HCG)"\cf0 \strokec4 , \cf7 \strokec7 7\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 8\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 9\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 10\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 1\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Pedi\'e1trica"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Villegas Rodr\'edguez Jos\'e9"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R4"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Utilidad de escalas de Parkland y Nassar para conversi\'f3n a cirug\'eda abierta en colecistectom\'eda dif\'edcil"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-04-06"\cf0 \strokec4 , \cf6 \strokec6 "2026-04-17"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-04-20"\cf0 \strokec4 , \cf6 \strokec6 "2027-05-01"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 9\cf0 \strokec4 : \cf6 \strokec6 "Oncocirug\'eda (CMN 20 Nov)"\cf0 \strokec4 , \cf7 \strokec7 11\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 12\cf0 \strokec4 : \cf6 \strokec6 "Rotaci\'f3n campo"\cf0 \strokec4 , \cf7 \strokec7 1\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Pedi\'e1trica"\cf0 \strokec4 , \cf7 \strokec7 2\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Pedi\'e1trica"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf5 \strokec5 # R3\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 "Almanza Ordu\'f1o Athmir Antonio"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R3"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Eficiencia de la safenoablaci\'f3n con l\'e1ser vs safenectom\'eda abierta en enfermedad venosa cr\'f3nica"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-06-15"\cf0 \strokec4 , \cf6 \strokec6 "2026-06-26"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-08-31"\cf0 \strokec4 , \cf6 \strokec6 "2026-09-11"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 3\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Vascular (HCG)"\cf0 \strokec4 , \cf7 \strokec7 6\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda de T\'f3rax (HCG)"\cf0 \strokec4 , \cf7 \strokec7 7\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Vascular (HCG)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Bueno L\'f3pez Daniela Alejandra"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R3"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Prevalencia de complicaciones locales tempranas y tard\'edas de pancreatitis aguda en el HCC"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-11-16"\cf0 \strokec4 , \cf6 \strokec6 "2026-11-27"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-01-18"\cf0 \strokec4 , \cf6 \strokec6 "2027-01-29"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 3\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (HGM)"\cf0 \strokec4 , \cf7 \strokec7 4\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Vascular (HCG)"\cf0 \strokec4 , \cf7 \strokec7 11\cf0 \strokec4 : \cf6 \strokec6 "Oncocirug\'eda (CMN 20 Nov)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Cordero Medina Marielos"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R3"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Utilidad de la escala Portsmouth-POSSUM para predecir morbilidad y mortalidad en cirug\'eda..."\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-06-01"\cf0 \strokec4 , \cf6 \strokec6 "2026-06-12"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-02-15"\cf0 \strokec4 , \cf6 \strokec6 "2027-02-26"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 8\cf0 \strokec4 : \cf6 \strokec6 "Oncocirug\'eda (CMN 20 Nov)"\cf0 \strokec4 , \cf7 \strokec7 10\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda de T\'f3rax (HCG)"\cf0 \strokec4 , \cf7 \strokec7 11\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda Vascular (HCG)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Ojeda Valenzuela Jos\'e9 Antonio"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R3"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Pruebas de funci\'f3n hep\'e1tica como predictores de coledocolitiasis"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-04-20"\cf0 \strokec4 , \cf6 \strokec6 "2026-05-01"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-02"\cf0 \strokec4 , \cf6 \strokec6 "2026-11-13"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 3\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda oncol\'f3gica (CMN 20 Nov)"\cf0 \strokec4 , \cf7 \strokec7 8\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda de t\'f3rax (HCG)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf5 \strokec5 # R2\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 "Angulo S\'e1nchez Rolando"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R2"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-03-02"\cf0 \strokec4 , \cf6 \strokec6 "2026-03-13"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-30"\cf0 \strokec4 , \cf6 \strokec6 "2026-12-11"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 4\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (ISSSTE)"\cf0 \strokec4 , \cf7 \strokec7 9\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda vascular (HCG)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Luna Borboa Jorge Luis"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R2"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2027-01-04"\cf0 \strokec4 , \cf6 \strokec6 "2027-01-15"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-30"\cf0 \strokec4 , \cf6 \strokec6 "2026-12-11"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 5\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (ISSSTE)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Maldonado Guardado Diana Guadalupe"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R2"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-07-06"\cf0 \strokec4 , \cf6 \strokec6 "2026-07-17"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-06-01"\cf0 \strokec4 , \cf6 \strokec6 "2026-06-12"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 11\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (ISSSTE)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Valenzuela Pardo Mariana"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R2"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-03-16"\cf0 \strokec4 , \cf6 \strokec6 "2026-03-27"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-02"\cf0 \strokec4 , \cf6 \strokec6 "2026-11-13"\cf0 \strokec4 )],\cb1 \
\cb3         \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\cf7 \strokec7 8\cf0 \strokec4 : \cf6 \strokec6 "Coloproctolog\'eda (ISSSTE)"\cf0 \strokec4 \}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf5 \strokec5 # R1\cf0 \cb1 \strokec4 \
\cb3     \cf6 \strokec6 "L\'f3pez F\'e9lix Jes\'fas Arturo"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R1"\cf0 \strokec4 , \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-05-18"\cf0 \strokec4 , \cf6 \strokec6 "2026-05-29"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-16"\cf0 \strokec4 , \cf6 \strokec6 "2026-11-27"\cf0 \strokec4 )], \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Portugal Beltran Emma"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R1"\cf0 \strokec4 , \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-04-20"\cf0 \strokec4 , \cf6 \strokec6 "2026-05-01"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-10-05"\cf0 \strokec4 , \cf6 \strokec6 "2026-10-16"\cf0 \strokec4 )], \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Rendon S\'e1nchez Manuel"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R1"\cf0 \strokec4 , \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-06-15"\cf0 \strokec4 , \cf6 \strokec6 "2026-06-26"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-01-18"\cf0 \strokec4 , \cf6 \strokec6 "2027-01-29"\cf0 \strokec4 )], \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Romero Molina Geovana Clarisa"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R1"\cf0 \strokec4 , \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-06-01"\cf0 \strokec4 , \cf6 \strokec6 "2026-06-12"\cf0 \strokec4 ), (\cf6 \strokec6 "2026-11-30"\cf0 \strokec4 , \cf6 \strokec6 "2026-12-11"\cf0 \strokec4 )], \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\}\cb1 \
\cb3     \},\cb1 \
\cb3     \cf6 \strokec6 "Valdez Valdez Ricardo Antonio"\cf0 \strokec4 : \{\cb1 \
\cb3         \cf6 \strokec6 "grado"\cf0 \strokec4 : \cf6 \strokec6 "R1"\cf0 \strokec4 , \cf6 \strokec6 "tesis"\cf0 \strokec4 : \cf6 \strokec6 "Por definir"\cf0 \strokec4 ,\cb1 \
\cb3         \cf6 \strokec6 "vacaciones"\cf0 \strokec4 : [(\cf6 \strokec6 "2026-07-06"\cf0 \strokec4 , \cf6 \strokec6 "2026-07-17"\cf0 \strokec4 ), (\cf6 \strokec6 "2027-02-01"\cf0 \strokec4 , \cf6 \strokec6 "2027-02-12"\cf0 \strokec4 )], \cf6 \strokec6 "rotaciones"\cf0 \strokec4 : \{\}\cb1 \
\cb3     \}\cb1 \
\cb3 \}\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Lista de clases (Muestra representativa basada en el programa)\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 CLASES = [\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-03"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Historia de la cirug\'eda"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "L\'f3pez F\'e9lix Jes\'fas Arturo"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Introducci\'f3n"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-04"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Asepsia y antisepsia"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Portugal Beltran Emma"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Introducci\'f3n"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-12"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "L\'edquidos y electrolitos en el paciente quir\'fargico"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "L\'f3pez F\'e9lix Jes\'fas Arturo"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Bases Quir\'fargicas"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-17"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Nutrici\'f3n en cirug\'eda"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Luna Borboa Jorge Luis"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Bases Quir\'fargicas"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-24"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Anatom\'eda anterior y posterior de la regi\'f3n inguinal"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Almanza Ordu\'f1o Athmir Antonio"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-25"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Fisiopatolog\'eda y Genesis herniaria"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Villegas Rodr\'edguez Jos\'e9"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-03-26"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Hernia ventral primaria"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Rendon S\'e1nchez Manuel"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-04-14"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Hernia inguinal"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Valdez Valdez Ricardo Antonio"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-04-15"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "T\'e9cnica quir\'fargica reparaci\'f3n Onlay"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Soto Valle Jos\'e9 Ema\'fas"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-04-28"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Manejo abierto y m\'ednima invasi\'f3n en hernia inguinal"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Cordero Medina Marielos"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Pared Abdominal"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-05-05"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Anatom\'eda quir\'fargica y fisiolog\'eda del es\'f3fago"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Portugal Beltran Emma"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda digestiva"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-05-06"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "ERGE y es\'f3fago de Barrett"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Rendon S\'e1nchez Manuel"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda digestiva"\cf0 \strokec4 \},\cb1 \
\cb3     \{\cf6 \strokec6 "fecha"\cf0 \strokec4 : \cf6 \strokec6 "2026-06-17"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 : \cf6 \strokec6 "Apendicitis aguda"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 : \cf6 \strokec6 "Maldonado Guardado Diana Guadalupe"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 : \cf6 \strokec6 "Cirug\'eda digestiva"\cf0 \strokec4 \}\cb1 \
\cb3 ]\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # FUNCIONES AUXILIARES\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  obtener_estado_residente(residente_nombre, fecha_actual):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     datos = RESIDENTES[residente_nombre]\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # Comprobar vacaciones\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  inicio, fin \cf2 \strokec2 in\cf0 \strokec4  datos[\cf6 \strokec6 "vacaciones"\cf0 \strokec4 ]:\cb1 \
\cb3         fecha_inicio = datetime.strptime(inicio, \cf6 \strokec6 "%Y-%m-%d"\cf0 \strokec4 ).date()\cb1 \
\cb3         fecha_fin = datetime.strptime(fin, \cf6 \strokec6 "%Y-%m-%d"\cf0 \strokec4 ).date()\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  fecha_inicio <= fecha_actual <= fecha_fin:\cb1 \
\cb3             \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 "\uc0\u55356 \u57140  Vacaciones"\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # Comprobar rotaciones (por mes)\cf0 \cb1 \strokec4 \
\cb3     mes_actual = fecha_actual.month\cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  mes_actual \cf2 \strokec2 in\cf0 \strokec4  datos[\cf6 \strokec6 "rotaciones"\cf0 \strokec4 ]:\cb1 \
\cb3         \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 f"\uc0\u55356 \u57317  Rotaci\'f3n: \cf0 \strokec4 \{datos['rotaciones'][mes_actual]\}\cf6 \strokec6 "\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 "\uc0\u9989  Hospital Civil (Servicio)"\cf0 \cb1 \strokec4 \
\
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 def\cf0 \strokec4  obtener_clases(fecha_actual):\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 # Convertimos strings a objetos date\cf0 \cb1 \strokec4 \
\cb3     clases_formateadas = []\cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  CLASES:\cb1 \
\cb3         c_copia = c.copy()\cb1 \
\cb3         c_copia[\cf6 \strokec6 "fecha_date"\cf0 \strokec4 ] = datetime.strptime(c[\cf6 \strokec6 "fecha"\cf0 \strokec4 ], \cf6 \strokec6 "%Y-%m-%d"\cf0 \strokec4 ).date()\cb1 \
\cb3         clases_formateadas.append(c_copia)\cb1 \
\cb3         \cb1 \
\cb3     \cf5 \strokec5 # Ordenar por fecha\cf0 \cb1 \strokec4 \
\cb3     clases_formateadas = \cf2 \strokec2 sorted\cf0 \strokec4 (clases_formateadas, key=\cf2 \strokec2 lambda\cf0 \strokec4  x: x[\cf6 \strokec6 "fecha_date"\cf0 \strokec4 ])\cb1 \
\cb3     \cb1 \
\cb3     clase_hoy = \cf2 \strokec2 next\cf0 \strokec4 ((c \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  clases_formateadas \cf2 \strokec2 if\cf0 \strokec4  c[\cf6 \strokec6 "fecha_date"\cf0 \strokec4 ] == fecha_actual), \cf2 \strokec2 None\cf0 \strokec4 )\cb1 \
\cb3     proximas_clases = [c \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  clases_formateadas \cf2 \strokec2 if\cf0 \strokec4  c[\cf6 \strokec6 "fecha_date"\cf0 \strokec4 ] > fecha_actual]\cb1 \
\cb3     proxima_clase = proximas_clases[\cf7 \strokec7 0\cf0 \strokec4 ] \cf2 \strokec2 if\cf0 \strokec4  proximas_clases \cf2 \strokec2 else\cf0 \strokec4  \cf2 \strokec2 None\cf0 \cb1 \strokec4 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 return\cf0 \strokec4  clase_hoy, proxima_clase\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # BARRA LATERAL (SIDEBAR)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 st.sidebar.image(\cf6 \strokec6 "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1a/Logo_de_la_Universidad_Aut%C3%B3noma_de_Sinaloa.svg/512px-Logo_de_la_Universidad_Aut%C3%B3noma_de_Sinaloa.svg.png"\cf0 \strokec4 , width=\cf7 \strokec7 150\cf0 \strokec4 )\cb1 \
\cb3 st.sidebar.title(\cf6 \strokec6 "Navegaci\'f3n"\cf0 \strokec4 )\cb1 \
\cb3 vista = st.sidebar.radio(\cf6 \strokec6 "Ir a:"\cf0 \strokec4 , [\cf6 \strokec6 "\uc0\u55356 \u57312  Inicio (Dashboard)"\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u55357 \u56424 \u8205 \u9877 \u65039  Perfil por Residente"\cf0 \strokec4 , \cf6 \strokec6 "\uc0\u55357 \u56517  Calendario de Clases"\cf0 \strokec4 ])\cb1 \
\
\cb3 st.sidebar.markdown(\cf6 \strokec6 "---"\cf0 \strokec4 )\cb1 \
\cb3 st.sidebar.markdown(\cf6 \strokec6 "### \uc0\u55357 \u56787 \u65039  Simulador de Fecha"\cf0 \strokec4 )\cb1 \
\cb3 st.sidebar.info(\cf6 \strokec6 "Cambia la fecha aqu\'ed para ver c\'f3mo se actualizan las guardias, vacaciones y rotaciones."\cf0 \strokec4 )\cb1 \
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # Por defecto iniciamos en la fecha sugerida por el PDF para demostraci\'f3n\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3 fecha_simulada = st.sidebar.date_input(\cf6 \strokec6 "Fecha actual:"\cf0 \strokec4 , date(\cf7 \strokec7 2026\cf0 \strokec4 , \cf7 \strokec7 3\cf0 \strokec4 , \cf7 \strokec7 30\cf0 \strokec4 ))\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # VISTA: INICIO (DASHBOARD)\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 if\cf0 \strokec4  vista == \cf6 \strokec6 "\uc0\u55356 \u57312  Inicio (Dashboard)"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     \cf5 \strokec5 # ENCABEZADO\cf0 \cb1 \strokec4 \
\cb3     col1, col2 = st.columns([\cf7 \strokec7 1\cf0 \strokec4 , \cf7 \strokec7 4\cf0 \strokec4 ])\cb1 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col1:\cb1 \
\cb3         st.image(\cf6 \strokec6 "https://cdn-icons-png.flaticon.com/512/2966/2966327.png"\cf0 \strokec4 , width=\cf7 \strokec7 100\cf0 \strokec4 ) \cf5 \strokec5 # Icono gen\'e9rico hospital/cirug\'eda\cf0 \cb1 \strokec4 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col2:\cb1 \
\cb3         st.title(\cf6 \strokec6 "Programa Operativo 2026-2027"\cf0 \strokec4 )\cb1 \
\cb3         st.subheader(\cf6 \strokec6 "Especialidad en Cirug\'eda General | CIDOCS / HCC"\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     st.markdown(\cf6 \strokec6 "---"\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # SECCI\'d3N: CLASES\cf0 \cb1 \strokec4 \
\cb3     clase_hoy, proxima_clase = obtener_clases(fecha_simulada)\cb1 \
\cb3     \cb1 \
\cb3     col_c1, col_c2 = st.columns(\cf7 \strokec7 2\cf0 \strokec4 )\cb1 \
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_c1:\cb1 \
\cb3         st.success(\cf6 \strokec6 "### \uc0\u55357 \u56538  Clase de Hoy"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  clase_hoy:\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Tema:** \cf0 \strokec4 \{clase_hoy['tema']\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**M\'f3dulo:** \cf0 \strokec4 \{clase_hoy['modulo']\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Imparte:** \uc0\u55357 \u56424 \u8205 \u9877 \u65039  \cf0 \strokec4 \{clase_hoy['ponente']\}\cf6 \strokec6  (\cf0 \strokec4 \{RESIDENTES[clase_hoy['ponente']]['grado']\}\cf6 \strokec6 )"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             st.info(\cf6 \strokec6 "No hay clase programada para el d\'eda de hoy."\cf0 \strokec4 )\cb1 \
\
\cb3     \cf2 \strokec2 with\cf0 \strokec4  col_c2:\cb1 \
\cb3         st.info(\cf6 \strokec6 "### \uc0\u55357 \u56604  Pr\'f3xima Clase"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  proxima_clase:\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Fecha:** \cf0 \strokec4 \{proxima_clase['fecha_date'].strftime('%d de %B, %Y')\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Tema:** \cf0 \strokec4 \{proxima_clase['tema']\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Imparte:** \uc0\u55357 \u56424 \u8205 \u9877 \u65039  \cf0 \strokec4 \{proxima_clase['ponente']\}\cf6 \strokec6  (\cf0 \strokec4 \{RESIDENTES[proxima_clase['ponente']]['grado']\}\cf6 \strokec6 )"\cf0 \strokec4 )\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             st.warning(\cf6 \strokec6 "No hay clases futuras registradas."\cf0 \strokec4 )\cb1 \
\
\cb3     st.markdown(\cf6 \strokec6 "---"\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # SECCI\'d3N: DISPONIBILIDAD DE RESIDENTES\cf0 \cb1 \strokec4 \
\cb3     st.markdown(\cf6 \strokec6 f"### \uc0\u55357 \u56525  Disponibilidad en el Servicio al **\cf0 \strokec4 \{fecha_simulada.strftime('%d/%m/%Y')\}\cf6 \strokec6 **"\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # Agrupar por grado\cf0 \cb1 \strokec4 \
\cb3     grados = [\cf6 \strokec6 "R4"\cf0 \strokec4 , \cf6 \strokec6 "R3"\cf0 \strokec4 , \cf6 \strokec6 "R2"\cf0 \strokec4 , \cf6 \strokec6 "R1"\cf0 \strokec4 ]\cb1 \
\cb3     \cb1 \
\cb3     tabs = st.tabs(grados)\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 for\cf0 \strokec4  i, grado \cf2 \strokec2 in\cf0 \strokec4  \cf2 \strokec2 enumerate\cf0 \strokec4 (grados):\cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  tabs[i]:\cb1 \
\cb3             res_grado = \{k: v \cf2 \strokec2 for\cf0 \strokec4  k, v \cf2 \strokec2 in\cf0 \strokec4  RESIDENTES.items() \cf2 \strokec2 if\cf0 \strokec4  v[\cf6 \strokec6 "grado"\cf0 \strokec4 ] == grado\}\cb1 \
\cb3             \cb1 \
\cb3             \cf5 \strokec5 # Crear un dataframe para mostrarlo bonito\cf0 \cb1 \strokec4 \
\cb3             datos_tabla = []\cb1 \
\cb3             \cf2 \strokec2 for\cf0 \strokec4  nombre, info \cf2 \strokec2 in\cf0 \strokec4  res_grado.items():\cb1 \
\cb3                 estado = obtener_estado_residente(nombre, fecha_simulada)\cb1 \
\cb3                 datos_tabla.append(\{\cf6 \strokec6 "Residente"\cf0 \strokec4 : nombre, \cf6 \strokec6 "Estado Actual"\cf0 \strokec4 : estado\})\cb1 \
\cb3                 \cb1 \
\cb3             df = pd.DataFrame(datos_tabla)\cb1 \
\cb3             \cb1 \
\cb3             \cf5 \strokec5 # Estilizar filas basado en el estado\cf0 \cb1 \strokec4 \
\cb3             \cf2 \strokec2 def\cf0 \strokec4  color_estado(val):\cb1 \
\cb3                 \cf2 \strokec2 if\cf0 \strokec4  \cf6 \strokec6 'Vacaciones'\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  val: \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 'background-color: #ffcccc; color: black'\cf0 \cb1 \strokec4 \
\cb3                 \cf2 \strokec2 elif\cf0 \strokec4  \cf6 \strokec6 'Rotaci\'f3n'\cf0 \strokec4  \cf2 \strokec2 in\cf0 \strokec4  val: \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 'background-color: #fff2cc; color: black'\cf0 \cb1 \strokec4 \
\cb3                 \cf2 \strokec2 else\cf0 \strokec4 : \cf2 \strokec2 return\cf0 \strokec4  \cf6 \strokec6 'background-color: #ccffcc; color: black'\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3             st.dataframe(df.style.applymap(color_estado, subset=[\cf6 \strokec6 'Estado Actual'\cf0 \strokec4 ]), use_container_width=\cf2 \strokec2 True\cf0 \strokec4 , hide_index=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # VISTA: PERFIL POR RESIDENTE\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 elif\cf0 \strokec4  vista == \cf6 \strokec6 "\uc0\u55357 \u56424 \u8205 \u9877 \u65039  Perfil por Residente"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.title(\cf6 \strokec6 "Buscador de Residentes \uc0\u55357 \u56589 "\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     lista_nombres = \cf2 \strokec2 list\cf0 \strokec4 (RESIDENTES.keys())\cb1 \
\cb3     residente_seleccionado = st.selectbox(\cf6 \strokec6 "Selecciona un residente:"\cf0 \strokec4 , lista_nombres)\cb1 \
\cb3     \cb1 \
\cb3     \cf2 \strokec2 if\cf0 \strokec4  residente_seleccionado:\cb1 \
\cb3         datos = RESIDENTES[residente_seleccionado]\cb1 \
\cb3         estado_actual = obtener_estado_residente(residente_seleccionado, fecha_simulada)\cb1 \
\cb3         \cb1 \
\cb3         col_p1, col_p2 = st.columns([\cf7 \strokec7 1\cf0 \strokec4 , \cf7 \strokec7 2\cf0 \strokec4 ])\cb1 \
\cb3         \cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_p1:\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"## \cf0 \strokec4 \{datos['grado']\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"### \cf0 \strokec4 \{residente_seleccionado\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.markdown(\cf6 \strokec6 f"**Estado hoy:** \cf0 \strokec4 \{estado_actual\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             st.image(\cf6 \strokec6 "https://cdn-icons-png.flaticon.com/512/3874/3874999.png"\cf0 \strokec4 , width=\cf7 \strokec7 150\cf0 \strokec4 ) \cf5 \strokec5 # Doctor icon\cf0 \cb1 \strokec4 \
\cb3             \cb1 \
\cb3         \cf2 \strokec2 with\cf0 \strokec4  col_p2:\cb1 \
\cb3             st.markdown(\cf6 \strokec6 "### \uc0\u55357 \u56534  Proyecto de Tesis"\cf0 \strokec4 )\cb1 \
\cb3             st.info(datos[\cf6 \strokec6 'tesis'\cf0 \strokec4 ])\cb1 \
\cb3             \cb1 \
\cb3             st.markdown(\cf6 \strokec6 "### \uc0\u55356 \u57140  Periodos Vacacionales"\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 for\cf0 \strokec4  inicio, fin \cf2 \strokec2 in\cf0 \strokec4  datos[\cf6 \strokec6 'vacaciones'\cf0 \strokec4 ]:\cb1 \
\cb3                 st.write(\cf6 \strokec6 f"- Del **\cf0 \strokec4 \{inicio\}\cf6 \strokec6 ** al **\cf0 \strokec4 \{fin\}\cf6 \strokec6 **"\cf0 \strokec4 )\cb1 \
\cb3                 \cb1 \
\cb3             st.markdown(\cf6 \strokec6 "### \uc0\u55356 \u57317  Rotaciones Externas (Meses)"\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 if\cf0 \strokec4  datos[\cf6 \strokec6 'rotaciones'\cf0 \strokec4 ]:\cb1 \
\cb3                 \cf2 \strokec2 for\cf0 \strokec4  mes, lugar \cf2 \strokec2 in\cf0 \strokec4  datos[\cf6 \strokec6 'rotaciones'\cf0 \strokec4 ].items():\cb1 \
\cb3                     meses = [\cf6 \strokec6 ""\cf0 \strokec4 , \cf6 \strokec6 "Ene"\cf0 \strokec4 , \cf6 \strokec6 "Feb"\cf0 \strokec4 , \cf6 \strokec6 "Mar"\cf0 \strokec4 , \cf6 \strokec6 "Abr"\cf0 \strokec4 , \cf6 \strokec6 "May"\cf0 \strokec4 , \cf6 \strokec6 "Jun"\cf0 \strokec4 , \cf6 \strokec6 "Jul"\cf0 \strokec4 , \cf6 \strokec6 "Ago"\cf0 \strokec4 , \cf6 \strokec6 "Sep"\cf0 \strokec4 , \cf6 \strokec6 "Oct"\cf0 \strokec4 , \cf6 \strokec6 "Nov"\cf0 \strokec4 , \cf6 \strokec6 "Dic"\cf0 \strokec4 ]\cb1 \
\cb3                     st.write(\cf6 \strokec6 f"- **\cf0 \strokec4 \{meses[mes]\}\cf6 \strokec6 :** \cf0 \strokec4 \{lugar\}\cf6 \strokec6 "\cf0 \strokec4 )\cb1 \
\cb3             \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3                 st.write(\cf6 \strokec6 "- Sin rotaciones externas asignadas en este ciclo."\cf0 \strokec4 )\cb1 \
\cb3                 \cb1 \
\cb3         st.markdown(\cf6 \strokec6 "---"\cf0 \strokec4 )\cb1 \
\cb3         st.markdown(\cf6 \strokec6 "### \uc0\u55356 \u57235  Clases a impartir y Sesiones Generales"\cf0 \strokec4 )\cb1 \
\cb3         \cb1 \
\cb3         \cf5 \strokec5 # Mostramos las clases donde el ponente sea \'e9l, o donde participen TODOS (como los viernes)\cf0 \cb1 \strokec4 \
\cb3         clases_residente = [c \cf2 \strokec2 for\cf0 \strokec4  c \cf2 \strokec2 in\cf0 \strokec4  CLASES \cf2 \strokec2 if\cf0 \strokec4  c[\cf6 \strokec6 "ponente"\cf0 \strokec4 ] == residente_seleccionado \cf2 \strokec2 or\cf0 \strokec4  c[\cf6 \strokec6 "ponente"\cf0 \strokec4 ] == \cf6 \strokec6 "Todos los Residentes"\cf0 \strokec4 ]\cb1 \
\cb3         \cf2 \strokec2 if\cf0 \strokec4  clases_residente:\cb1 \
\cb3             df_clases = pd.DataFrame(clases_residente)[[\cf6 \strokec6 "fecha"\cf0 \strokec4 , \cf6 \strokec6 "tipo"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 ]]\cb1 \
\cb3             df_clases.columns = [\cf6 \strokec6 "Fecha"\cf0 \strokec4 , \cf6 \strokec6 "Tipo"\cf0 \strokec4 , \cf6 \strokec6 "M\'f3dulo"\cf0 \strokec4 , \cf6 \strokec6 "Tema"\cf0 \strokec4 , \cf6 \strokec6 "Ponente"\cf0 \strokec4 ]\cb1 \
\cb3             st.table(df_clases)\cb1 \
\cb3         \cf2 \strokec2 else\cf0 \strokec4 :\cb1 \
\cb3             st.write(\cf6 \strokec6 "No tiene clases programadas en la base de datos actual."\cf0 \strokec4 )\cb1 \
\
\pard\pardeftab720\partightenfactor0
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # VISTA: CALENDARIO DE CLASES\cf0 \cb1 \strokec4 \
\cf5 \cb3 \strokec5 # ==========================================\cf0 \cb1 \strokec4 \
\pard\pardeftab720\partightenfactor0
\cf2 \cb3 \strokec2 elif\cf0 \strokec4  vista == \cf6 \strokec6 "\uc0\u55357 \u56517  Calendario de Clases"\cf0 \strokec4 :\cb1 \
\pard\pardeftab720\partightenfactor0
\cf0 \cb3     st.title(\cf6 \strokec6 "Calendario Completo de Clases Acad\'e9micas"\cf0 \strokec4 )\cb1 \
\cb3     st.write(\cf6 \strokec6 "Temario de unidades did\'e1cticas y expositores"\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     df_all_clases = pd.DataFrame(CLASES)[[\cf6 \strokec6 "fecha"\cf0 \strokec4 , \cf6 \strokec6 "tipo"\cf0 \strokec4 , \cf6 \strokec6 "modulo"\cf0 \strokec4 , \cf6 \strokec6 "tema"\cf0 \strokec4 , \cf6 \strokec6 "ponente"\cf0 \strokec4 ]]\cb1 \
\cb3     df_all_clases.columns = [\cf6 \strokec6 "Fecha"\cf0 \strokec4 , \cf6 \strokec6 "Tipo"\cf0 \strokec4 , \cf6 \strokec6 "M\'f3dulo"\cf0 \strokec4 , \cf6 \strokec6 "Tema de la Clase"\cf0 \strokec4 , \cf6 \strokec6 "Ponente"\cf0 \strokec4 ]\cb1 \
\cb3     \cb1 \
\cb3     \cf5 \strokec5 # A\'f1adir grado al df\cf0 \cb1 \strokec4 \
\cb3     df_all_clases[\cf6 \strokec6 "Grado"\cf0 \strokec4 ] = df_all_clases[\cf6 \strokec6 "Ponente"\cf0 \strokec4 ].\cf2 \strokec2 apply\cf0 \strokec4 (\cf2 \strokec2 lambda\cf0 \strokec4  x: RESIDENTES.get(x, \{\}).get(\cf6 \strokec6 "grado"\cf0 \strokec4 , \cf6 \strokec6 ""\cf0 \strokec4 ))\cb1 \
\cb3     \cb1 \
\cb3     st.dataframe(df_all_clases, use_container_width=\cf2 \strokec2 True\cf0 \strokec4 , hide_index=\cf2 \strokec2 True\cf0 \strokec4 )\cb1 \
\cb3     \cb1 \
\cb3     st.caption(\cf6 \strokec6 "Nota: El calendario est\'e1 sujeto a cambios por parte de la Jefatura de Ense\'f1anza."\cf0 \strokec4 )\cb1 \
}