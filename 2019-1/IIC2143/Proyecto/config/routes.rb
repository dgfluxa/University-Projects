# frozen_string_literal: true

Rails.application.routes.draw do
  get 'moderated_courses/update'

  get 'messages/create'

  get 'messages/index'

  resources :conversations do
    resources :messages
  end

  get 'occupied_rooms/new'

  get 'occupied_rooms/create'

  get 'occupied_rooms/edit'

  get 'occupied_rooms/update'

  get 'occupied_rooms/destroy'

  get 'like_coments/destroy'

  get 'like_coments/create'

  get 'favorite_publications/update'

  get 'subscribed_users/update'

  get 'study_room_valorations/new'

  get 'study_room_valorations/create'

  get 'study_room_valorations/edit'

  get 'study_room_valorations/update'

  get 'study_room_valorations/destroy'

  get 'ofertclases/clases_particulares', to: 'ofertclases#clases_particulares'

  get 'professor_courses/update'

  resources :buscoclases

  resources :ofertclases

  get 'study_groups/new'

  get 'study_groups/create'

  post 'study_groups/create'

  get 'study_groups/edit'

  get 'study_groups/update'

  get 'study_groups/index'

  get 'study_groups/destroy'

  get 'student_courses/update'

  get '/profile/:id', to: 'pages#profile', as: 'profile'

  get 'paso', to: 'pages#paso', as: 'paso'

  get 'paso/course/:id', to: 'pages#paso2', as: 'paso_room'

  get 'paso/course/:course_id/study_room/:room_id', to: 'study_groups#new', as: 'paso_final'

  post 'paso/course/:course_id/study_room/:room_id', to: 'study_groups#create', as: 'grupo_creado'

  get 'moderators', to: 'pages#moderators', as: 'moderators'

  get 'administrators', to: 'pages#administrators', as: 'administrators'

  get 'requests', to: 'pages#requests', as: 'requests'

  post 'courses/:course_id', to: 'publicacions#create', as: 'publicada'

  post 'profile/:id', to: 'conversations#create', as: 'nueva_conversacion'

  post 'conversation/:conversation_id/messages', to: 'messages#create', as: 'nuevo_mensaje'

  post 'clases_particulares', to: 'pages#busqueda', as: 'buscador'
  post 'busco_particulares', to: 'pages#busqueda2', as: 'buscador2'
  post 'study_group', to: 'pages#busqueda_grupos', as: 'buscador_grupo'
  post 'courses/:course_id/publicacions/:publicacion_id/publicacion_comments/:id', to: 'publicacion_comments#create'
  post 'course/:id', to: 'pages#busqueda_publicacion', as: 'buscador_publicacion'
  post 'courses', to: 'pages#busqueda_cursos', as: 'buscador_curso'
  get 'estadisticas', to: 'pages#estadisticas'
  get 'busco_particulares', to: 'pages#busco_particulares'

  get '/clases_particulares', to: 'pages#clases_particulares', as: 'clases_particulares'
  get 'study_groups', to: 'pages#study_groups', as: 'study_groups'
  get 'conversation/:conversation_id/messages', to: 'pages#imbox', as: 'imbox'
  get 'imbox', to: 'pages#imbox'
  get 'clases_particulares', to: 'pages#busqueda', as: 'mostrar_busqueda'
  get 'course/:id', to: 'courses#show'

  get '/make_admin/:user_id', to: 'pages#make_admin', as: 'make_admin'

  get '/delete_user/:user_id', to: 'pages#delete_user', as: 'delete_user'

  devise_for :users
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
  resources  :camps do
    resources :study_rooms
  end

  resources :courses do
    resources :publicacions do
      resources :likes
    end
    resources :moderation_requests
  end

  resources :study_rooms do
    resources :study_room_comments
  end

  resources :study_rooms do
    resources :study_room_valorations
  end

  resources :study_rooms do
    resources :occupied_rooms
  end

  resources :courses do
    resources :publicacions do
      resources :publicacion_comments do
        resources :like_coments
      end
    end
  end

  resources :study_groups

  get 'ofertclases/_form0', to: 'ofertclases#_form0', as: 'ofrecer_clase'

  post 'ofertclases', to: 'ofertclases#create', as: 'ofrecer'
  patch 'ofertclases/:id', to: 'ofertclases#update', as: 'editarclase'
  patch 'buscoclases/:id', to: 'buscoclases#update', as: 'editar_anuncio'
  patch 'courses/:course_id/publicacions/:id', to: 'publicacions#update', as: 'publicar_edit'
  post 'buscoclases', to: 'buscoclases#create', as: 'anunciar'
  post 'buscoclases/:id', to: 'buscoclases#create', as: 'agregar'
  post 'moderated_courses/update'
  root 'pages#home'
  get 'ofertclases/clases_particulares', to: 'ofertclases#clases_particulares', as: 'anuncios'
  post 'publicacions', to: 'publicacions#create', as: 'publicar'
end
