# frozen_string_literal: true

class Camp < ApplicationRecord
  has_many :study_rooms, dependent: :destroy

  validates :nombre, presence: true
  validates :ubicacion, presence: true
  validates :url, presence: true
end
