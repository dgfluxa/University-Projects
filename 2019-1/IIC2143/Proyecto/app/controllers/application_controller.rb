# frozen_string_literal: true

class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception
  before_action :authenticate_user!
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up) { |u| u.permit(:first_name, :last_name, :email, :password) }

    devise_parameter_sanitizer.permit(:account_update) { |u| u.permit(:first_name, :last_name, :email, :password, :current_password, :avatar) }
  end

  def student_course_text
    @student_course_exists ? 'Desuscribirse como alumno' : 'Suscribirse como alumno'
  end

  def professor_course_text
    @professor_course_exists ? 'Desuscribirse como profesor' : 'Suscribirse como profesor'
  end

  def subscribed_user_text
    @subscribed_user_exists ? 'Salir del grupo' : 'Unirse al grupo'
  end

  def favorite_publication_text
    @favorite_publication_exists ? 'Eliminar de Favoritos' : 'Agregar a Favoritos'
  end

  helper_method :favorite_publication_text
  helper_method :subscribed_user_text
  helper_method :student_course_text
  helper_method :professor_course_text
end
