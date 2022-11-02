# frozen_string_literal: true

class Publicacion < ApplicationRecord
  validates :titulo, presence: true
  validates :description, presence: true
  validates :contenido, presence: true
  belongs_to :course
  belongs_to :user
  has_many :publicacion_comments, dependent: :destroy
  has_many :likes, dependent: :destroy
  has_many :favorite_publications, dependent: :destroy
end
