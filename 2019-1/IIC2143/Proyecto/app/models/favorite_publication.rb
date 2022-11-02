# frozen_string_literal: true

class FavoritePublication < ApplicationRecord
  belongs_to :publicacion, optional: false
  belongs_to :user, optional: false
end
