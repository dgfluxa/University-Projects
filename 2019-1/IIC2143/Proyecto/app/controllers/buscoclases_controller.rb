# frozen_string_literal: true

class BuscoclasesController < ApplicationController
  def new
    @buscoclases = Buscoclase.new
  end

  def index
    @buscoclases = Buscoclase.new
    @cursos_buscados = Buscoclase.all
    @clases_ofrecidas = Ofertclase.all
    @courses = Course.all
  end

  def create
    @agregar_user = Buscoclase.new(agregar_users_params)
    if !@agregar_user.user.nil?
      @anuncio = Buscoclase.find(params[:id])
      @agregar_user = Buscoclase.new(agregar_users_params)
      @agregar_user.course = @anuncio.course
      @agregar_user.time = @anuncio.time
      @agregar_user.id_grupo = @anuncio.id_grupo
      if @agregar_user.save
        redirect_to @agregar_user
      else
        @anuncio = Buscoclase.find(params[:id])
        redirect_to buscoclase_path(@anuncio)
      end
    else
      @buscoclases = Buscoclase.new(busco_clases_params)
      @buscoclases.user = current_user.email
      @id_grupo = Buscoclase.last
      @id_grupo = if !@id_grupo.nil?
                    @id_grupo.id_grupo + 1
                  else
                    1
                  end
      @buscoclases.id_grupo = @id_grupo
      if @buscoclases.save
        redirect_to busco_particulares_path
      else
        redirect_to busco_particulares_path
      end
    end
  end

  def show
    @buscoclases = Buscoclase.find(params[:id])
    @agregar_user = Buscoclase.new
    @anuncios = Buscoclase.all
    @id_group = @buscoclases.id_grupo
  end

  def destroy
    @buscoclases = Buscoclase.find(params[:id])
    Buscoclase.where('id_grupo = ?', @buscoclases.id_grupo).each(&:destroy)
    redirect_to clases_particulares_path
  end

  def update
    @clase = Buscoclase.find(params[:id])
    @nuevo = Buscoclase.new(busco_clases_params)
    Buscoclase.where('id_grupo = ?', @clase.id_grupo).each do |user|
      user.update(busco_clases_params) if @nuevo.time != ''
    end
    redirect_to clases_particulares_path
  end

  private

  def busco_clases_params
    params.require(:buscoclase).permit(:course, :time)
  end

  def agregar_users_params
    params.require(:buscoclase).permit(:user)
  end
end
