# frozen_string_literal: true

class Buscoclase < ApplicationRecord
  validates :user, presence: true
  validates :time, presence: true
  validates :course, presence: true
end
