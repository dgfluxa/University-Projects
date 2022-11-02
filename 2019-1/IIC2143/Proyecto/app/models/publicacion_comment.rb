# frozen_string_literal: true

class PublicacionComment < ApplicationRecord
  belongs_to :user
  belongs_to :publicacion
  has_many :like_coments, dependent: :destroy
end
