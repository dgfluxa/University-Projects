# frozen_string_literal: true

class FavoritePublicationsController < ApplicationController
  load_and_authorize_resource
  def update
    favorite_publication = FavoritePublication.where(publicacion: Publicacion.find(params[:publicacion]), user: current_user)
    if favorite_publication == []
      FavoritePublication.create(publicacion: Publicacion.find(params[:publicacion]), user: current_user)
      @favorite_publication_exists = true
    else
      favorite_publication.destroy_all
      @favorite_publication_exists = false
    end
    respond_to do |format|
      format.html {}
      format.js { render inline: 'location.reload();' }
    end
  end
end
