# frozen_string_literal: true

# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alatside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
Course.create(name: 'Ingeniería de Software', sigla: 'IIC2143', description: 'Este curso enseña técnicas para llevar
  a cabo un verdadero proyecto de desarrollo de software, desde el descubrimiento y la especificación de los
  requisitos, al interactuar con el cliente y/o usuarios, a la aplicación, experimentación y demostración de una
  solicitud que cumple los requisitos.')
Course.create(name: 'Programación Avanzada', sigla: 'IIC2233', description:
  'Este curso enseña técnicas para el diseñar, códificar, probar y evaluar programas que resuelven problemas
  algorítmicos a partir de las especificaciones detalladas. En particular, el curso enseña algunas construcciones
   avanzadas de programación orientada a objetos no incluidas en el curso introductorio, algunas estructuras de datos
   fundamentales, diseño básico de algoritmos y técnicas de análisis. Los estudiantes deben usar una serie de
   herramientas de programación para desarrollar sus programas.')
Course.create(name: 'Optimización', sigla: 'ICS1113', description: 'Este curso pretende capacitar al alumnos en:
  la formulación de modelos de optimización para problemas de tomas de decisiones en el ámbito determinístico, en
  diferentes áreas de la ingeniería y en el uso de técnicas de caracterización y resolución de modelos determinísticos
  de optimización, utilizando diversos algoritmos de programación lineal y no lineal')
Course.create(name: 'Introducción a la Programación', sigla: 'IIC1103', description: 'Este curso enseña a resolver
  problemas algorítmicos mediante la programación de computadores. En particular, el curso enseña los fundamentos
  de la programación -cómo especificar los datos que describen un problema y cómo diseñar algoritmos que puedan
  procesar esos datos- y su aplicación a la resolución de una variedad de tipos de problemas. El curso hace énfasis
  en el estilo de de programación orientada a objetos, en las estructuras de datos fundamentales, y en los algoritmos
  fundamentales. Los alumnos deben usar herramientas de programación para desarrollar sus programas.')
Course.create(name: 'Bases de Datos', sigla: 'IIC2413', description: 'Este curso enseña la teoría básica del modelo relacional y su aplicación al diseño de bases de datos relacionales, incluidas las transacciones y la integración de datos, normalización, y procedimientos almacenados. El curso también enseña el lenguaje SQL y conceptos fundamentales de los sistemas de gestión de bases de datos (DBMS).')
Course.create(name: 'Álgebra Lineal', sigla: 'MAT1203', description: 'Proporcionar al alumno los conceptos principales y la terminología del álgebra lineal que permitan al alumno plantear, resolver y analizar mediante técnicas vectoriales y matriciales problemas que surgen en el ámbito de la ingeniería, como por ejemplo en diseño de estructuras, análisis de señales, sistemas de control, robótica, computación gráfica, física, análisis estadístico y simulaciones.')
Course.create(name: 'Cálculo I', sigla: 'MAT1610', description: 'El curso se orienta a entregar los conceptos básicos de límites y continuidad de funciones, de la derivada de una función y su interpretación geométrica, en conjunto con los mecanismos y técnicas de derivación, las aplicaciones más relevantes de la derivada a problemas diversos de las matemáticas y la física, la obtención de puntos críticos de una función, la definición de la Integral, el cálculo de integrales mediante primitivas, y las técnicas de integración.')
Course.create(name: 'Cálculo II', sigla: 'MAT1620', description: 'El curso proporciona los conceptos fundamentales de las aplicaciones de la integral a diversos problemas de ingeniería, del análisis y cálculo de series y sucesiones, de geometría vectorial, y del análisis de curvas planas y en el espacio.')
Course.create(name: 'Cálculo III', sigla: 'MAT1630', description: 'El curso proporciona al alumno los conocimientos básicos de cálculo diferencial de funciones escalares y vectoriales de varias variables, de integrales múltiples sobre regiones más generales, y los conceptos y métodos de integrales de línea y superficie.')
Camp.create(nombre: 'Casa Central', ubicacion: "Av Libertador Bernardo O'Higgins 340, Santiago, Región Metropolitana", url: 'https://goo.gl/maps/u1To3SHmghZazfAcA')
Camp.create(nombre: 'San Joaquin', ubicacion: 'Av. Vicuña Mackenna 4860, Macul, Región Metropolitana', url: 'https://goo.gl/maps/vFphbuok2PQB88PA6')
Camp.create(nombre: 'Oriente', ubicacion: 'Jaime Guzmán Errázuriz 3300, Providencia, Región Metropolitana', url: 'https://goo.gl/maps/YGZqJhaE1XyZ9AbFA')
Camp.create(nombre: 'Lo Contador', ubicacion: 'El Comendador 1916, Providencia, Región Metropolitana', url: 'https://goo.gl/maps/PMLR5rnej9194QD6A')
Camp.create(nombre: 'Villarrica', ubicacion: "Bernardo O'Higgins 501, Villarrica, Región de la Araucanía", url: 'https://goo.gl/maps/UjQLxmCmY9M9xYip9')

StudyRoom.create(name: 'Salas Biblioteca', ubication: 'San Joaquin', camp_id: 2)
StudyRoom.create(name: 'Salas Biblioteca Humanidades', ubication: 'San Joaquin', camp_id: 2)
StudyRoom.create(name: 'Sala Multipropósito', ubication: 'Campus Oriente', camp_id: 3)
StudyRoom.create(name: 'Salas Biblioteca de Derecho y Comunicaciones', ubication: 'Casa Central', camp_id: 1)

User.create(first_name: 'Brayan', last_name: 'Moreno', email: 'bbmoreno@uc.cl', password: 'grupo10software', admin: true)
User.create(first_name: 'Tairon', last_name: 'Garrido', email: 'tngarrido@uc.cl', password: 'grupo10software', admin: true)
User.create(first_name: 'Diego', last_name: 'Fluxá', email: 'dgfluxa@uc.cl', password: 'grupo10software', admin: true)
User.create(first_name: 'Javier', last_name: 'Parra', email: 'jparra@uc.cl', password: 'grupo10software')
User.create(first_name: 'Oliver', last_name: 'Perez', email: 'operez@uc.cl', password: 'grupo10software')
User.create(first_name: 'Alejandro', last_name: 'Font', email: 'afont@uc.cl', password: 'grupo10software')
User.create(first_name: 'Eva', last_name: 'Cano', email: 'ecano@uc.cl', password: 'grupo10software')
User.create(first_name: 'Patricia', last_name: 'Blanco', email: 'pblanco@uc.cl', password: 'grupo10software')
User.create(first_name: 'Sara', last_name: 'Puig', email: 'spuig@uc.cl', password: 'grupo10software')
