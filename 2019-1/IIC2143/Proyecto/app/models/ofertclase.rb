# frozen_string_literal: true

class Ofertclase < ApplicationRecord
  validates :precio, presence: true
  validates :time, presence: true
  validates :description, presence: true
  validates :course, presence: true
end
